def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (35 <= s.index(char) <= 40 and ')' <= char <= 'l')]
    return ''.join(filtered_chars)