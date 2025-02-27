def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (27 <= i <= 85 and 'c' <= s[i] <= 'i'):
            result += s[i]
    return result