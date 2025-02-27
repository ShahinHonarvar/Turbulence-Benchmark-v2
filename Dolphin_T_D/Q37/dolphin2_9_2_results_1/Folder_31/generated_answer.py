def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 57 or i > 96 or s[i] < '*' or (s[i] > 'w'):
            result += s[i]
    return result