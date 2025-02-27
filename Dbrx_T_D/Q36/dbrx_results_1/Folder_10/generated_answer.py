def filter_chars(s: str) -> str:
    for i in range(35, 60):
        char = s[i]
        if '!' < char < 'B':
            s = s.replace(char, '', 1)
    return s