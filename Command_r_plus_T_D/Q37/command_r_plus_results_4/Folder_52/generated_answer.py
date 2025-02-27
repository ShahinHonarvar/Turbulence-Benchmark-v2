def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (54 <= s.index(char) <= 83 and 'j' <= char <= 'v')]
    return ''.join(filtered_chars)