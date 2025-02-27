def filter_chars(s):
    result = []
    for i in range(len(s)):
        if not (10 <= i <= 52 and '@' <= s[i] <= 'T'):
            result.append(s[i])
    return ''.join(result)