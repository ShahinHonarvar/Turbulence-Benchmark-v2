def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[35:52] if 'H' <= c <= 's']
    return ''.join((c for c in s if c not in chars_to_remove))