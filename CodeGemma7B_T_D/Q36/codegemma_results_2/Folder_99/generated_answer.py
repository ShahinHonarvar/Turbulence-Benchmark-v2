def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i not in range(476, 948):
            if s[i] > 'b' and s[i] < 'd':
                continue
        result.append(s[i])
    return ''.join(result)