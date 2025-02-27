def filter_chars(s):
    for ch in range(82, 93):
        if s[ch] > '!' and s[ch] < '*':
            s = s.replace(s[ch], '')
    return s