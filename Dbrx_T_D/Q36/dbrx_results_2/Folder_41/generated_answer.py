def filter_chars(input_string: str) -> str:
    return ''.join((char for char in input_string if not (81 < input_string.index(char) < 89 and 'f' < char < '{')))