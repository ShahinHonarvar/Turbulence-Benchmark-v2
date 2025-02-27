def filter_chars(s: str) -> str:
    for i in range(33, 36):
        if chr(i) > '>' and chr(i) < 'A':
            s = s.replace(chr(i), '')
    return s