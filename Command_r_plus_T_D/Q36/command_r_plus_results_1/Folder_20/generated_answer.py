def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not 60 < ord(char) < 67]
    return ''.join(filtered_chars)