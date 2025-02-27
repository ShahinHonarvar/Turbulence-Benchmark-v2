def filter_chars(s):
    t = list(s)
    for i in range(43, 68):
        if i < len(s):
            if s[i] > 't' and s[i] < 'x':
                c = s[i]
                for j in range(len(t)):
                    if t[j] == c:
                        t[j] = ''
    return ''.join(t)