def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 7 or i > 8 or s[i] < 'B' or (s[i] > 'H'):
            result.append(s[i])
    return ''.join(result)