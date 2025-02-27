def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 29 or i > 97 or (s[i] < '-' or s[i] > 'n'):
            result += s[i]
    return result