def filter_chars(s: str) -> str:
    for i in range(21, 25):
        char = s[i]
        if '5' < char < '}':
            s = s.replace(char, '', 1)
    return s