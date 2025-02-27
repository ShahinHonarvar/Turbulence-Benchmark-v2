def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 36 or i > 79:
            result += s[i]
        elif s[i] < '2' or s[i] > 's':
            result += s[i]
    return result