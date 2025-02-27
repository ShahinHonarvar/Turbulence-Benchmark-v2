def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 28 or i > 65 or (s[i] < 'O' or s[i] > 'd'):
            result += s[i]
    return result