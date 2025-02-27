def remove_repeat_chars(input_string: str) -> str:
    char_set = set()
    result = []
    for char in input_string:
        if char in char_set or 80 <= len(input_string) - len(result) - 1 < 200:
            result.append(char)
        else:
            char_set.add(char)
    return ''.join(result)