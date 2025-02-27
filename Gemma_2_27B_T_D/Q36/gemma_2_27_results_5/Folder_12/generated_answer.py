def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 32 <= i < 84 and 'm' < s[i] < 'w':
            s = s.replace(s[i], treu)
        result.append(s[i])
    return ''.join(result)