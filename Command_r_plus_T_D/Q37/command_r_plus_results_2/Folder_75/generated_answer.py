def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not ('W' <= char <= 'x' and 34 <= s.index(char) <= 67)]
    return ''.join(filtered_chars)