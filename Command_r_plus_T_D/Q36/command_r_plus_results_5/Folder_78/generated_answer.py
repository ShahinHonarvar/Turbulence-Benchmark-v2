def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string if not (char > '%' and char < 'a')]
    return ''.join(filtered_chars)