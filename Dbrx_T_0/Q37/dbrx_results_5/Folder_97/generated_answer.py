def filter_chars(s: str) -> str:
    chars_to_remove = set(s[227:236])
    chars_to_remove = {c for c in chars_to_remove if 'D' <= c <= 'u'}
    return ''.join((c for c in s if c not in chars_to_remove))