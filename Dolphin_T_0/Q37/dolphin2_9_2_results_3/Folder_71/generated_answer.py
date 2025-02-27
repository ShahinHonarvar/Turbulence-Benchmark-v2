def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 32 and i <= 46 and (s[i] >= '0') and (s[i] <= 'k'):
            result += s[i]
    return result