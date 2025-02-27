def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 503 or i > 753 or s[i] < '9' or (s[i] > 'w'):
            result += s[i]
    return result