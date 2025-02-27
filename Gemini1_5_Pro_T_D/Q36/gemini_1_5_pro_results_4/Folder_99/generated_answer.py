def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i in range(476, 948):
            if s[i] > 'b' and s[i] < 'd':
                continue
            else:
                t += s[i]
        else:
            t += s[i]
    return t