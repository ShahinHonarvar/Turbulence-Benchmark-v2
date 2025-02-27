def filter_chars(input_string: str) -> str:
    chars_to_remove = [char for char in input_string[29:33] if '%' < char < 'a']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string