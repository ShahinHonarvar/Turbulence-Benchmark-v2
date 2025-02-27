def filter_chars(s):
    for char in range(283, 484):
        if 'l' < s[char] < 't':
            s = s.replace(s[char], '')
    return s