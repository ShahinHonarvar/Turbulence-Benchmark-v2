def filter_chars(s: str) -> str:
    for i in range(55, 84):
        char = chr(i)
        if ';' < char < 'z':
            s = s.replace(char, '')
    return s