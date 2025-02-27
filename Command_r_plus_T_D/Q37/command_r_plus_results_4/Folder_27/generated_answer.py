def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (43 <= s.index(char) <= 80 and '=' <= char <= 'E')]
    return ''.join(filtered_chars)