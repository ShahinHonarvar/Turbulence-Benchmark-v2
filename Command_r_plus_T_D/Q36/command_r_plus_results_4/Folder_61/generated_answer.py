def filter_chars(input_string: str) -> str:
    chars_to_remove = set((char for char in input_string[3:9] if '*' < char < 'E'))
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result