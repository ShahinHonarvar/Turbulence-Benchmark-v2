def filter_chars(s: str) -> str:
    for i in range(90, 97):
        char = chr(i)
        if char > 'j' and char < 'w':
            s = s.replace(char, '')
    return s