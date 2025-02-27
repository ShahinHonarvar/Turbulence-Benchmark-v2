def filter_chars(s):
    for char in range(55, 80):
        if s[char] > 'S' and s[char] < 's':
            s = s.replace(s[char], '')
    return s