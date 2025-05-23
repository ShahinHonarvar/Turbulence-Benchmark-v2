def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 41 <= s.index(char) <= 79 or not 'f' <= char <= '|']
    return ''.join(filtered_chars)