def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 19 <= s.index(char) <= 32 and 'f' <= char <= 'o']
    return ''.join(filtered_chars)