def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not '?' < char < 'k']
    return ''.join(filtered_chars)