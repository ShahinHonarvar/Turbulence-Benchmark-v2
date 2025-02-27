def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 69 < i < 97 and 'V' < s[i] < 'j':
            continue
        t += s[i]
    return t