def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 45 and i < 57 and (s[i] > 'F') and (s[i] < 'n'):
            c = s[i]
            t = ''
            for k in range(len(s)):
                if s[k] != c:
                    t += s[k]
            s = t
    return s