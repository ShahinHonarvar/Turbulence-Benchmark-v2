def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i in range(86, 93) and s[i] >= '!' and (s[i] <= 's'):
            pass
        else:
            result += s[i]
    return result