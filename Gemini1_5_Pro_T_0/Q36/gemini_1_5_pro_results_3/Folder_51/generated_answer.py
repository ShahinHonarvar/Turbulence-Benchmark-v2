def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 58 and i < 81 and (s[i] > '5') and (s[i] < '>'):
            continue
        else:
            t += s[i]
    return t