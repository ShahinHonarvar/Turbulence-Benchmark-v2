def filter_chars(input_string: str) -> str:
    chars_to_remove = [char for char in input_string[78:81] if 'S' < char < '[']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string