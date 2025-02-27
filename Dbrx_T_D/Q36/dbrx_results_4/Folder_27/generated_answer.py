def filter_chars(s: str) -> str:
    for i in range(48, 75):
        if i > ord('6') and i < ord('_'):
            s = s.replace(chr(i), '', 1)
    return s