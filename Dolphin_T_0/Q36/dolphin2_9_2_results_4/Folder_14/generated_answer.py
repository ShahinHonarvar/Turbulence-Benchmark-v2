def filter_chars(s):
    for ch in range(41, 56):
        if 'Z' < s[ch] < 'c':
            s = s.replace(s[ch], '')
    return s