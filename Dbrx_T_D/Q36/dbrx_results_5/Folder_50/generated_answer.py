def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 80 >= ord(c) > 37 or (c < 'q' and (61 > ord(c) >= 56 or 88 <= ord(c) < 113))))