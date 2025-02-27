def remove_repeat_chars(input_string: str) -> str:
    char_set = set()
    result = []
    for char in input_string:
        if 68 <= len(result) < 99:
            if char in char_set:
                continue
            char_set.add(char)
        result.append(char)
    return ''.join(result)