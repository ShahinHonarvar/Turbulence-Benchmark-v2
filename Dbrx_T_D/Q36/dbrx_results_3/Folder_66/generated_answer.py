def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if 39 < ord(char) < 87 or ord(char) <= ord('!') or ord(char) >= ord('}')]
    return ''.join(filtered_chars)