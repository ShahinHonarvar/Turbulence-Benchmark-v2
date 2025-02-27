def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 27 and i < 75 and (s[i] > 'A') and (s[i] < 'i'):
            for c in s[i:]:
                if c != s[i]:
                    t += c
            return t
    return s