def filter_chars(s):
    for i in range(13, 29):
        if i < len(s) and 'c' <= s[i] <= 'n':
            char = s[i]
            s = s.replace(char, '')
    return s