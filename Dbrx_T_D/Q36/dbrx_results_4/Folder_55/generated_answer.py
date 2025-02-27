def filter_chars(s: str) -> str:
    for i in range(3, 5):
        char = s[i]
        if ord('Y') < ord(char) < ord('s'):
            s = s.replace(char, '', 1)
    return s