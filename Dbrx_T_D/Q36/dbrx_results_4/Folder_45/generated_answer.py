def filter_chars(s: str) -> str:
    for i in range(81, 86):
        char = s[i]
        if '!' < char < 's':
            s = s.replace(char, '', 1)
    return s