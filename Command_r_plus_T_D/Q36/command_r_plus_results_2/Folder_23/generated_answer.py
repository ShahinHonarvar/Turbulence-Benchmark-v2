def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not (21 < input_string.index(char) < 25 and '5' < char < '}')]
    return ''.join(filtered_chars)