def filter_chars(s):
    for char in range(722, 833):
        if s[char] >= 'K' and s[char] <= 'm':
            s = s.replace(s[char], '')
    return s