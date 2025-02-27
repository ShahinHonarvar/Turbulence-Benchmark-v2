def filter_chars(s: str) -> str:
    for i in range(1, 7):
        char = s[i]
        if '3' < char < '^':
            s = s.replace(char, '', i)
    return s