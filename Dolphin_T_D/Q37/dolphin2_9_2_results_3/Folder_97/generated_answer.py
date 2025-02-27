def filter_chars(s):
    for char in range(227, 235):
        if 'D' <= s[char] <= 'u':
            s = s.replace(s[char], '')
    return s