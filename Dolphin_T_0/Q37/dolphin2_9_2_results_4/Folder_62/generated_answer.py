def filter_chars(s):
    for i in range(len(s)):
        if i >= 10 and i <= 69 and (s[i] >= 'I') and (s[i] <= 'K'):
            s = s.replace(s[i], '')
    return s