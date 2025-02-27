def filter_chars(s: str) -> str:
    chars_to_remove = set(s[503:754]) & set('9:;<=>?@ABCDEFGHIJKLMNOPQRSTUVW')
    return ''.join((c for c in s if c not in chars_to_remove))