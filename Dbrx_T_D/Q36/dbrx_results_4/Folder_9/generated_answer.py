def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 50 or i >= 92:
            result += s[i]
        elif s[i] > 'A' and s[i] < 'Q':
            result = result[:-1]
    return result