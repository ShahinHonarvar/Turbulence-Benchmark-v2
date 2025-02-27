def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not 17 <= i <= 63 or (s[i] < 'O' or s[i] > '^'):
            result += s[i]
    return result