def filter_chars(s):
    for char in range(86, 93):
        if 'E' < s[char] < '~':
            s = s.replace(s[char], '')
    return s