def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[86:94] if 'E' < ch < '~']
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s