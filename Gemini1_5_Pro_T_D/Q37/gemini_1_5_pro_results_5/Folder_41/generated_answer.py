def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (26 <= i <= 64 and 'V' <= c <= 'o'):
            result += c
    return result