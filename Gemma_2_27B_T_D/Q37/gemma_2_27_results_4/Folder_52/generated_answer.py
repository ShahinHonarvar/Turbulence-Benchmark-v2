def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 54 or i > 83 or s[i] < 'j' or (s[i] > 'v'):
            result.append(s[i])
    return ''.join(result)