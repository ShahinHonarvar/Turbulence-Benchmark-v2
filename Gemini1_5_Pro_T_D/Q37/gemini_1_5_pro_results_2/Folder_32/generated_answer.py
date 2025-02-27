def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i >= 23 and i <= 89 and (s[i] >= 'w') and (s[i] <= '{'):
            if s[i] not in t:
                t += s[i]
        else:
            t += s[i]
    r = ''
    for c in s:
        if c not in t:
            r += c
    return r