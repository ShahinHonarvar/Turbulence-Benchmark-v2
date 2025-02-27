def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 17 or i > 63 or (s[i] < 'O' or s[i] > '^'):
            result += s[i]
    return result