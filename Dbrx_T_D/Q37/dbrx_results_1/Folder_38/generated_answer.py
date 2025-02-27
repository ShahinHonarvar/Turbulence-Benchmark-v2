def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 24 or i > 79 or (s[i] < 'a' or s[i] > 'f'):
            result += s[i]
    return result