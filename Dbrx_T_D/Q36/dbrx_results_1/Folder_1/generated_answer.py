def filter_chars(s: str) -> str:
    return ''.join((char for char in s if s.index(char) <= 68 or s.index(char) >= 87 or (not '#' < char < 'L')))