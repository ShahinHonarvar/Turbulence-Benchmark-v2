def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 35 and i <= 40 and (s[i] >= ')') and (s[i] <= 'l'):
            continue
        result += s[i]
    return result