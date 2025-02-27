def filter_chars(s):
    for char in range(4, 8):
        if s[char] > '1' and s[char] < 'J':
            s = s.replace(s[char], '')
    return s