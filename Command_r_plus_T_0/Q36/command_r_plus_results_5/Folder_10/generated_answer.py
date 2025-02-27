def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not '!' < char < 'B']
    return ''.join(filtered_chars)