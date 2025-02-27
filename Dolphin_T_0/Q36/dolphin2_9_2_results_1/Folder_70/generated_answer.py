def filter_chars(s):
    for i in range(170, 195):
        char = s[i]
        if char > '!' and char < '{':
            s = s.replace(char, '')
    return s