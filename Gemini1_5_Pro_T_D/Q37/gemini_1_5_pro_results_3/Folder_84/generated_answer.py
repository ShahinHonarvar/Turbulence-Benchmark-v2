def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        c = s[i]
        if 138 <= i <= 920 and '6' <= c <= 'A':
            new_s = new_s.replace(c, '')
        else:
            new_s += c
    return new_s