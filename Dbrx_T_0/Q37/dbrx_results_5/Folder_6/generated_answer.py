def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 13 <= s.index(char) <= 28 and 'c' <= char <= 'n']
    return ''.join(filtered_chars)