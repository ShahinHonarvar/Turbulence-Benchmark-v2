def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not ('P' <= char <= 'x' and 12 <= s.index(char) <= 25)]
    return ''.join(filtered_chars)