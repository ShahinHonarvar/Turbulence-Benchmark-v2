def filter_chars(s: str) -> str:
    return ''.join((char for char in s if s.index(char) < 58 or s.index(char) > 81 or (not '5' < char < '>')))