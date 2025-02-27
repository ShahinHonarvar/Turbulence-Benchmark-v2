def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[40:63] if '7' < ch < 'H']
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s