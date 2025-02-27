def filter_chars(s):
    for char in range(77, 87):
        if s[char] > ';' and s[char] < 'r':
            s = s.replace(s[char], '')
    return s