def filter_chars(s):
    for char in range(11, 46):
        if '!' < s[char] < 'A':
            s = s.replace(s[char], '')
    return s