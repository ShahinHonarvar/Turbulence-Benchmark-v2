def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 75 >= ord(c) > 56 or (c < 'a' and 95 > ord(c) >= 18)))