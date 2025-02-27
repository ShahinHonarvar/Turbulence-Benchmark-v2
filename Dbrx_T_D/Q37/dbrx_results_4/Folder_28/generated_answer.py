def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 20 or i > 79 or (s[i] < '!' or s[i] > 'T'):
            result += s[i]
    return result