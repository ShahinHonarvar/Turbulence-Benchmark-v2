def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (25 <= i <= 97 and 'm' <= s[i] <= 'w'):
            result += s[i]
    return result