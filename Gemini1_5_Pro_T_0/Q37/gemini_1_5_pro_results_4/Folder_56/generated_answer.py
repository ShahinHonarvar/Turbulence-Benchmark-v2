def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 71 <= i <= 94 and 'K' <= s[i] <= 'a':
            for c in s:
                if c != s[i]:
                    t += c
            s = t
            t = ''
        else:
            t += s[i]
    return t