def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 5 or i > 6 or (not 'G' <= s[i] <= 'p'):
            result.append(s[i])
    return ''.join(result)