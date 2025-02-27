def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 11 < i < 46 and '!' < s[i] < 'A':
            continue
        t += s[i]
    return t