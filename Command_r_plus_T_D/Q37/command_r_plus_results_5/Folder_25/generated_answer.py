def filter_chars(input_string: str) -> str:
    chars_to_remove = [char for char in input_string if 31 <= ord(char) <= 38 and ';' <= char <= 'g']
    return ''.join((char for char in input_string if char not in chars_to_remove))