def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 77 <= i <= 87 and ';' < s[i] < 'r':
            continue
        else:
            t += s[i]
    return t