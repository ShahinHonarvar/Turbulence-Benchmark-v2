def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 27 or i > 85 or (s[i] < 'c' or s[i] > 'i'):
            result += s[i]
    return result