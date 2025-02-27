def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (38 <= s.index(char) <= 99 and 'A' <= char <= 'Q')]
    return ''.join(filtered_chars)