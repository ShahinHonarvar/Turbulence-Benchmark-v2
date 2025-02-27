def filter_chars(s):
    for char in range(1, 9):
        if '8' < s[char] < 'm':
            s = s.replace(s[char], '')
    return s