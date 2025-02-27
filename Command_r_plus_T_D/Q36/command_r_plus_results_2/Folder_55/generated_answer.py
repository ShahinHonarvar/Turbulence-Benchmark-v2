def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not 'Y' < char < 's']
    return ''.join(filtered_chars)