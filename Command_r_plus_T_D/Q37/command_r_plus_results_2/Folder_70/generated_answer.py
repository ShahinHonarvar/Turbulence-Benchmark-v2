def filter_chars(s: str) -> str:
    chars_to_remove = set(s[515:539]) & set('+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    return ''.join((c for c in s if c not in chars_to_remove))