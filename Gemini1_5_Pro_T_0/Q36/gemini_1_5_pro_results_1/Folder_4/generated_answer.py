def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 42 < i < 67 and '6' < s[i] < 'g':
            continue
        else:
            t += s[i]
    return t