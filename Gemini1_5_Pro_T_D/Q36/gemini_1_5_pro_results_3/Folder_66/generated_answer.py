def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 39 <= i <= 87 and '!' < s[i] < '}':
            t = t + ''
        else:
            t = t + s[i]
    return t