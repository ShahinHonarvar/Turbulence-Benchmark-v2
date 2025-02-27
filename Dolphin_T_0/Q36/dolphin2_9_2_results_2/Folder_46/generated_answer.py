def filter_chars(s):
    for ch in range(19, 69):
        if s[ch] > '<' and s[ch] < 'C':
            s = s.replace(s[ch], '')
    return s