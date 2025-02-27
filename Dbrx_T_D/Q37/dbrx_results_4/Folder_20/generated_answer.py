def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not (25 <= input_string.index(char) <= 97 and 'm' <= char <= 'w')]
    return ''.join(filtered_chars)