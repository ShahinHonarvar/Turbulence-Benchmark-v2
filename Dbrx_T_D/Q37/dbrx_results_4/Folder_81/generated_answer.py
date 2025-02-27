def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if 19 <= input_string.index(char) <= 92 and '8' <= char <= 'm']
    return ''.join(filtered_chars)