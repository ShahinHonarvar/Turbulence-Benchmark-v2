def filter_chars(s: str) -> str:
    for c in range(ord('O'), ord('^') + 1):
        for i in range(17, 64):
            s = s.replace(chr(c), '')
    return s