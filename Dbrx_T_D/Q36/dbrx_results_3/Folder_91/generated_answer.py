def filter_chars(s: str) -> str:
    return ''.join((char for char in s[1:4] if ord('$') < ord(char) < ord('?'))) + s[4:]