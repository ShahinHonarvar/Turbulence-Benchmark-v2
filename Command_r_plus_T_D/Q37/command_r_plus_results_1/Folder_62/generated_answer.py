def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (10 <= s.index(char) <= 69 and 'I' <= char <= 'K')]
    return ''.join(filtered_chars)