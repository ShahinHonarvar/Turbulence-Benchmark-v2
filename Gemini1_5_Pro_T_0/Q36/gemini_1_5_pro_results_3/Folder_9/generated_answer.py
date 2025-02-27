def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 50 and i < 92 and (s[i] > 'A') and (s[i] < 'Q'):
            continue
        t += s[i]
    return t