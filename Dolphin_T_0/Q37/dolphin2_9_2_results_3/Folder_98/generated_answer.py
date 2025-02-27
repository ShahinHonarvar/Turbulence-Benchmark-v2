def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 8 or i > 9 or (s[i] < 'R' or s[i] > 't'):
            result += s[i]
    return result