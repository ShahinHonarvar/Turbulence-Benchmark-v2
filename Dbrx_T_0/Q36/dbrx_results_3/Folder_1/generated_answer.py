def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 69 <= s.index(c) < 87 and ord('#') < ord(c) < ord('L')))