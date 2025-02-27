def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 81 <= i <= 89 and 'f' < s[i] < '{':
            continue
        t += s[i]
    return t