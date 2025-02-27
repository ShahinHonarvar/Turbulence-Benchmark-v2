def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 43 <= i <= 80 and '=' <= s[i] <= 'E':
            pass
        else:
            result += s[i]
    return result