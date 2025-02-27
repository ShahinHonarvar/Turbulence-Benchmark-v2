def filter_chars(input_string: str) -> str:
    chars_to_remove = [char for char in input_string[38:55] if 'colon' <= char <= 'r']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string