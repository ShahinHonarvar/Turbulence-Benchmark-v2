def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 46 < i < 68 and 'H' < s[i] < 's':
            continue
        t += s[i]
    return t