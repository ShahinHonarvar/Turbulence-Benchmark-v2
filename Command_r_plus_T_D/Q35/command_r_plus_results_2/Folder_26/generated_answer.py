def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[68:99])
    for char in repeat_chars:
        input_string = input_string.replace(char, '')
    return input_string