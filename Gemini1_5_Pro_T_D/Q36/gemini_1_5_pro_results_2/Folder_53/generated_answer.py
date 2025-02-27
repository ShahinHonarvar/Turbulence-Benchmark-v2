def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 90 < i < 97 and 'j' < s[i] < 'w':
            for c in s:
                if c != s[i]:
                    t += c
            s = t
            t = ''
        else:
            t += s[i]
    return t