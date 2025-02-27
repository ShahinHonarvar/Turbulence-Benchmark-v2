def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (51 <= s.index(char) <= 96 and 'X' <= char <= 'p')]
    return ''.join(filtered_chars)