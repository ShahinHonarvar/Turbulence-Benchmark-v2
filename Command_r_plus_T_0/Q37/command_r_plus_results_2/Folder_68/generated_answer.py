def filter_chars(s: str) -> str:
    chars_to_remove = set(s[7:10]) & set('6789:;<=>?@ABCD')
    return ''.join((c for c in s if c not in chars_to_remove))