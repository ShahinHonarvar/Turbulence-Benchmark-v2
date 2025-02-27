def filter_chars(s: str) -> str:
    chars_to_remove = set(s[43:59]) & set('6789ABC')
    return ''.join((c for c in s if c not in chars_to_remove))