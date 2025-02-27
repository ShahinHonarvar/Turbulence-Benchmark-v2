def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 114 or i > 639 or (s[i] < '!' or s[i] > 'x'):
            result += s[i]
    return result