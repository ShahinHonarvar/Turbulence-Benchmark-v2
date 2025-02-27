def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (43 <= i <= 80 and '=' <= s[i] <= 'E'):
            result += s[i]
    return result