def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 23 and i < 83 and (s[i] > 'f') and (s[i] < 'o'):
            for c in s:
                if c != s[i]:
                    t += c
            s = t
            t = ''
        else:
            t += s[i]
    return t