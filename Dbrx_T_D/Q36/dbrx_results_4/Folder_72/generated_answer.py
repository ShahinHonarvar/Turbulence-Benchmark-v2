def filter_chars(s: str) -> str:
    for char in sorted(set(s[44:68])):
        if 'W' < char < 'x':
            s = s.replace(char, '')
    return s