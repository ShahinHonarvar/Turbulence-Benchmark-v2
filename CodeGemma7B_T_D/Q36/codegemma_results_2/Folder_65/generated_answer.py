def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 58 or i >= 82 or (s[i] <= 'F' or s[i] >= 'O'):
            result.append(s[i])
    return ''.join(result)