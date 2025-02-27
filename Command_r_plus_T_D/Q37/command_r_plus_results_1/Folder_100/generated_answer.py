def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (88 <= s.index(char) <= 90 and 'J' <= char <= 'Q')]
    return ''.join(filtered_chars)