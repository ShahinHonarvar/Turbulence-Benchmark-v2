def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (29 <= i <= 97 and '-' <= c <= 'n'):
            result += c
    return result