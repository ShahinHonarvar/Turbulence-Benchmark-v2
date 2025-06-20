def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[58:81] if '5' < c < '>']
    return ''.join((c for c in s if c not in chars_to_remove))