def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 81 <= i <= 89 and 'f' < s[i] < '{':
            continue
        if 81 <= i <= 89:
            t += s[i]
        elif not (81 < i < 89 and 'f' < s[i] < '{'):
            t += s[i]
    return t