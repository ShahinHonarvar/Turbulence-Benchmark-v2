def filter_chars(s):
    for char in range(170, 195):
        if s[char] > '!' and s[char] < '}':
            s = s.replace(s[char], '')
    return s