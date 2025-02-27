def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not ('R' <= char <= 't' and 8 <= s.index(char) <= 9)]
    return ''.join(filtered_chars)