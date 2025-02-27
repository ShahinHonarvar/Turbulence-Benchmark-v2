def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not '3' < char < '^']
    return ''.join(filtered_chars)