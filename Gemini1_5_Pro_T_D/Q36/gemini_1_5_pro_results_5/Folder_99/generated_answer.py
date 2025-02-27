def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 476 and i < 948 and (s[i] > 'b') and (s[i] < 'd'):
            continue
        if s[i] in t:
            continue
        t += s[i]
    return t