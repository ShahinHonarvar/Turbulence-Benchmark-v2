def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 72 < i < 93 and '<' < s[i] < 'J':
            continue
        t += s[i]
    return t