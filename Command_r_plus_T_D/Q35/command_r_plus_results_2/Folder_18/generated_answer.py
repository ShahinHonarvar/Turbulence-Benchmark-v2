def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[56:90])
    for char in repeat_chars:
        if input_string.count(char) > 1:
            input_string = input_string.replace(char, '')
    return input_string