def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 'A' < char < 'h']
    return ''.join(filtered_chars)