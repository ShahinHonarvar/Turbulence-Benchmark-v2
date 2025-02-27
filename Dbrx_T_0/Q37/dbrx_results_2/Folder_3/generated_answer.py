def filter_chars(input_string: str) -> str:
    return ''.join((char for char in input_string if not (37 <= input_string.index(char) <= 56 and '6' <= char <= '_')))