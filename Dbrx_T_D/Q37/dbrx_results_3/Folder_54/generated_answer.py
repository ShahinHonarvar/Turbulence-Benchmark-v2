def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if (i < 46 or i > 85) and (s[i] < '-' or s[i] > 'X'):
            result += s[i]
    return result