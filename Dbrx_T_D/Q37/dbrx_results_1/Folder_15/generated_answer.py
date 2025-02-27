def filter_chars(s: str) -> str:
    return ''.join((char for char in s if not ('?' <= char <= 'f' and 2 <= s.index(char) <= 6)))