def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 476 <= i <= 948 and 'b' < s[i] < 'd':
            continue
        else:
            t += s[i]
    return t