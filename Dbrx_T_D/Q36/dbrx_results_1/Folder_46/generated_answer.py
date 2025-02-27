def filter_chars(s: str) -> str:
    return ''.join((char for char in s if 19 < s.index(char) < 69 or (char > '<' and char < 'C') or s.index(char) >= 69))