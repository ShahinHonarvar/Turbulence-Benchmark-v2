def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[2:7] if 'h' < ch < 'k']
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s