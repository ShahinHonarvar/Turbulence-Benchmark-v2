def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if 36 <= input_string.index(char) <= 56 and char < '6' or char > '_']
    return ''.join(filtered_chars)