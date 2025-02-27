def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 309 <= i <= 591 and 'S' < s[i] < 'm':
            continue
        t += s[i]
    return t