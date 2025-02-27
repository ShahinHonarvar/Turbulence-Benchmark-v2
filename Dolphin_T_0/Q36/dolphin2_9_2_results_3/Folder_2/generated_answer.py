def filter_chars(s):
    for ch in range(421, 854):
        if 'D' < s[ch] < 'J':
            s = s.replace(s[ch], '')
    return s