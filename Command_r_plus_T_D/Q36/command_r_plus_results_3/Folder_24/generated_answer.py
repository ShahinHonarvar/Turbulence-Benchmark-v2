def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 't' < char < 'v']
    return ''.join(filtered_chars)