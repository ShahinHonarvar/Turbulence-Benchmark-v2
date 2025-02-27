def filter_chars(s):
    for char in range(24, 37):
        if 'A' < s[char] < 'h':
            s = s.replace(s[char], '')
    return s