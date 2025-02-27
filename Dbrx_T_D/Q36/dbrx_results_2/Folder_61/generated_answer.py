def filter_chars(s: str) -> str:
    for i in range(max(3, 0), min(len(s), 9)):
        char = s[i]
        if char > '*' and char < 'E':
            s = s.replace(char, '', 1)
    return s