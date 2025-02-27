def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (33 <= i <= 70 and '7' <= c <= 'k'):
            result += c
    return result