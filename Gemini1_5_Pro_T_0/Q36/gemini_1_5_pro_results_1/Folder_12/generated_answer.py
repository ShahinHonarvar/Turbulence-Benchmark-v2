def filter_chars(s):
    result = []
    for i in range(len(s)):
        c = s[i]
        if 32 < i < 84 and 'm' < c < 'w':
            continue
        result.append(c)
    return ''.join(result)