def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 19 or i > 90 or (s[i] < 'F' or s[i] > 'h'):
            result += s[i]
    return result