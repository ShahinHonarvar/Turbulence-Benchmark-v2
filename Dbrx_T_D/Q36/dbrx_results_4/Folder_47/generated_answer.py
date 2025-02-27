def filter_chars(s: str) -> str:
    start, end = (45, 57)
    for i in range(start, end):
        char = chr(i)
        if 'F' < char < 'n':
            s = s.replace(char, '', end)
    return s