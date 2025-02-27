def filter_chars(s):
    for char in range(57, 69):
        if ' ' < s[char] < 'W':
            s = s.replace(s[char], '')
    return s