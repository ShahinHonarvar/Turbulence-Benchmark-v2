def filter_chars(s):
    for char in range(318, 337):
        if 'B' < s[char] < 'z':
            s = s.replace(s[char], '')
    return s