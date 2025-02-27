def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i >= 12 and i <= 25 and (s[i] >= 'P') and (s[i] <= 'x'):
            for c in s:
                if c != s[i]:
                    t += c
            s = t
            t = ''
        else:
            t += s[i]
    return t