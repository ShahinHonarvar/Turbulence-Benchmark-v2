def filter_chars(s: str) -> str:
    for i in range(90, 97):
        if chr(i) > 'j' and chr(i) < 'w':
            s = s.replace(chr(i), '')
    return s