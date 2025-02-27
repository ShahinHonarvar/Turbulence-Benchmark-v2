def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (51 <= s.index(char) <= 77 and 'V' <= char <= 'Y')]
    return ''.join(filtered_chars)