def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 'a' <= char < 'f']
    return ''.join(filtered_chars)