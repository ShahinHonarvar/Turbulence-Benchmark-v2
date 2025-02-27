def filter_chars(s: str) -> str:
    chars_to_remove = set(s[71:95])
    chars_to_remove = {c for c in chars_to_remove if 'K' <= c <= 'a'}
    return ''.join((c for c in s if c not in chars_to_remove))