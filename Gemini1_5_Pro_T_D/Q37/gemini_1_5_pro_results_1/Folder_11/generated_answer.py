def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (29 <= i <= 97 and '-' <= s[i] <= 'n'):
            result += s[i]
    return result