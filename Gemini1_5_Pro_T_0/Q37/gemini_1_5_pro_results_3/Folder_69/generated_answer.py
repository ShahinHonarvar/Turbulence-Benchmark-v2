def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (114 <= i <= 639 and '!' <= c <= 'x'):
            result += c
    return result