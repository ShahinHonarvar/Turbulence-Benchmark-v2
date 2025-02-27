def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (19 <= s.index(char) <= 92 and '8' <= char <= 'm')]
    return ''.join(filtered_chars)