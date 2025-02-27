def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[18:64] if '3' < ch < 'B']
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s