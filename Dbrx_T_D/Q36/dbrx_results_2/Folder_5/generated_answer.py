def filter_chars(s: str) -> str:
    for i in range(55, 66):
        char = s[i]
        if 'f' < char < '|':
            s = s.replace(char, '', 1)
    return s