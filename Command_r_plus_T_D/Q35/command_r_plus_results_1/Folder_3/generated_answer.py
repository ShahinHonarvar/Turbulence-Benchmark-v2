def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[56:88])
    result = []
    for char in input_string:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)