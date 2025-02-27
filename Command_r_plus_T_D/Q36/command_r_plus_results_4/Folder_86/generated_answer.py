def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[672:709] if 'X' < c < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s