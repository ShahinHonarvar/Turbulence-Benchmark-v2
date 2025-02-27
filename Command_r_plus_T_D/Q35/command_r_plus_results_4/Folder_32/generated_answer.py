def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[86:90])
    result = ''
    for char in input_string:
        if char not in repeat_chars:
            result += char
    return result