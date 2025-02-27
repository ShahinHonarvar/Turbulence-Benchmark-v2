def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 58 < i < 82 and 'F' < s[i] < 'O':
            continue
        else:
            t += s[i]
    return t