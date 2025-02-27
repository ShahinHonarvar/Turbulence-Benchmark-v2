def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i >= 36 and i <= 40 and (s[i] >= 'H') and (s[i] <= 'e'):
            if s[i] not in t:
                t += s[i]
        else:
            t += s[i]
    r = ''
    for c in t:
        if c not in s[36:41] or c < 'H' or c > 'e':
            r += c
    for i in range(len(s)):
        if s[i] in r:
            r = r.replace(s[i], '', 1)
    for c in t:
        if c in s[36:41] and c >= 'H' and (c <= 'e'):
            r += c
    return r