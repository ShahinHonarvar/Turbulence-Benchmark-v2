def filter_chars(input_string: str) -> str:
    return ''.join((char for char in input_string if not (25 <= input_string.index(char) <= 97 and 'm' <= char <= 'w')))