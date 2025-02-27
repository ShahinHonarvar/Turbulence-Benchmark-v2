def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not 90 <= ord(c) < 97 or not 'j' < c < 'w'))