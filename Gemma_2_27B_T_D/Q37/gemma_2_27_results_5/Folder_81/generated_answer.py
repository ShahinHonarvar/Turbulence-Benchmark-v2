def filter_chars(s):
    result = []
    for i in range(len(s)):
        if not (19 <= i <= 92 and '8' <= s[i] <= 'm'):
            result.append(s[i])
    return ''.join(result)