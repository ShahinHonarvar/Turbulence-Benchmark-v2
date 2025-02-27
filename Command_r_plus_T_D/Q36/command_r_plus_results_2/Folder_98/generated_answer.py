def filter_chars(s: str) -> str:
    chars_to_remove = set(s[4:8]) & set('23456789ABCDEFGHI')
    return ''.join((c for c in s if c not in chars_to_remove))