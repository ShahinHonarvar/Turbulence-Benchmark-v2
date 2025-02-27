def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i >= 27 and i <= 29 and (s[i] >= ';') and (s[i] <= 'b'):
            continue
        if s[i] in s[27:30] and s[i] >= ';' and (s[i] <= 'b'):
            continue
        t += s[i]
    return t