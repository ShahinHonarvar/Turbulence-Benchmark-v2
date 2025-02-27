def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 45 < i < 57 and 'F' < s[i] < 'n':
            continue
        else:
            t += s[i]
    return t