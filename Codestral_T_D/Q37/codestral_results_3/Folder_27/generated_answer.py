def filter_chars(s):
    for char in sorted(set(s[43:81])):
        if '=' <= char <= 'E':
            s = s.replace(char, '')
    return s