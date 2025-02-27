def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 69 and i < 97 and (s[i] > 'V') and (s[i] < 'j'):
            continue
        else:
            t += s[i]
    return t