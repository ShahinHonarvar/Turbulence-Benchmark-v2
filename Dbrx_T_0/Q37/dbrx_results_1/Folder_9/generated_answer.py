def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 38 <= s.index(char) <= 99 and 'A' <= char <= 'Q']
    return ''.join((char for char in s if char not in filtered_chars))