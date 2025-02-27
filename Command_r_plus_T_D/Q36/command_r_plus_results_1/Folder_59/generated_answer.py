def filter_chars(input_string: str) -> str:
    chars_to_remove = set((char for char in input_string[3:8] if '?' < char < 'k'))
    return ''.join((char for char in input_string if char not in chars_to_remove))