def filter_chars(s: str) -> str:
    for ch in s[60:71]:
        if '0' <= ch <= '@':
            s = s.replace(ch, '')
    return s