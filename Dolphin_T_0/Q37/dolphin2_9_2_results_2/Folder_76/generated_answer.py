def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 379 or i > 898 or s[i] < 'M' or (s[i] > 'v'):
            result += s[i]
    return result