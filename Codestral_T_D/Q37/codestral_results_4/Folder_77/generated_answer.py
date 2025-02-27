def filter_chars(s):
    for char in s[384:412]:
        if '/' <= char <= '8':
            s = s.replace(char, '')
    return s