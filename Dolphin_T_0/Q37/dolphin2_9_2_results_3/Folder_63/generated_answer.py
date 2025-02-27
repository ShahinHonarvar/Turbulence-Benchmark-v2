def filter_chars(s):
    for char in range(42, 93):
        if s[char] >= '/' and s[char] <= 'a':
            s = s.replace(s[char], '')
    return s