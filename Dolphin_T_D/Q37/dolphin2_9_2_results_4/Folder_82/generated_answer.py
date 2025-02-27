def filter_chars(s):
    for char in range(12, 26):
        if 'P' <= s[char] <= 'x':
            s = s.replace(s[char], '')
    return s