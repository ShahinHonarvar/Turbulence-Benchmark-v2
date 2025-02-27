def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not ('G' <= char <= 'p' and 5 <= s.index(char) <= 6)]
    return ''.join(filtered_chars)