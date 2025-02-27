def filter_chars(s):
    for char in range(33, 36):
        if s[char] > '>' and s[char] < 'A':
            s = s.replace(s[char], '')
    return s