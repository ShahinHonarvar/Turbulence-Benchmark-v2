def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 24 and i <= 79 and (s[i] >= 'a') and (s[i] <= 'f'):
            result = result + s[i]
    return result