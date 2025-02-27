def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (34 <= s.index(char) <= 67 and 'W' <= char <= 'x')]
    return ''.join(filtered_chars)