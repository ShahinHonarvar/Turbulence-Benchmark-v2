def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (18 <= i <= 81 and 'W' <= s[i] <= '['):
            result += s[i]
    return result