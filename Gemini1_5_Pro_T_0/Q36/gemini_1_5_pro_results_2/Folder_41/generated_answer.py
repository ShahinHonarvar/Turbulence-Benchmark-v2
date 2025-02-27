def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 81 and i < 89 and (s[i] > 'f') and (s[i] < '{'):
            t += ''
        else:
            t += s[i]
    return t