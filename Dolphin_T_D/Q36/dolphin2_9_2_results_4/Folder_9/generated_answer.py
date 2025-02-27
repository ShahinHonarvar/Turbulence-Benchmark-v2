def filter_chars(s):
    for i in range(50, 92):
        char = s[i]
        if char > 'A' and char < 'Q':
            s = s.replace(char, '')
    return s