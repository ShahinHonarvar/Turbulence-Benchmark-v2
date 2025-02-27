def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i > 4 and i < 4 and (s[i] >= '7') and (s[i] <= 'o'):
            continue
        result += s[i]
    return result