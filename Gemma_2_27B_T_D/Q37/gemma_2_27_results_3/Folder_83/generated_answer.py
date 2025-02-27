def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 29 or i > 79 or s[i] < 'K' or (s[i] > 'z'):
            result.append(s[i])
    return ''.join(result)