def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if 36 <= input_string.index(char) <= 79 and '2' <= char <= 's']
    return ''.join(filtered_chars)