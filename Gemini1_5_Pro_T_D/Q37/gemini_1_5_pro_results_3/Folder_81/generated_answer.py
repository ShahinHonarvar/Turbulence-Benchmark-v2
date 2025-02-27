def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (19 <= i <= 92 and '8' <= c <= 'm'):
            result += c
    return result