def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (373 <= s.index(char) <= 901 and 'T' <= char <= 'h')]
    return ''.join(filtered_chars)