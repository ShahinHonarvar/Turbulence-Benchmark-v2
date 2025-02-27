def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not ord('!') < ord(char) < ord('A')]
    return ''.join(filtered_chars)