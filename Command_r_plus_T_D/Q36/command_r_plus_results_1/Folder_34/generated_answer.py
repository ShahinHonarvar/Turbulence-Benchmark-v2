def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (10 < char < 79 and '?' < char < 'm')]
    return ''.join(filtered_chars)