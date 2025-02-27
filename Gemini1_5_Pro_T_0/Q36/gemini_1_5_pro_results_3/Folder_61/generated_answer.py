def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 3 <= i <= 9:
            if not '*' < s[i] < 'E':
                t += s[i]
        else:
            t += s[i]
    s = t
    t = ''
    for i in range(len(s)):
        if 3 <= i <= 9:
            if '*' < s[i] < 'E':
                t += ''
            else:
                t += s[i]
        else:
            t += s[i]
    return t