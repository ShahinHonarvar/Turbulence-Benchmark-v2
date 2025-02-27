def filter_chars(s: str) -> str:
    chars_to_remove = set(s[379:899]) & set('MNOPQRSTUVWXYZ[\\]^_`mnoqrsuvwxyz{|}~')
    return ''.join((ch for ch in s if ch not in chars_to_remove))