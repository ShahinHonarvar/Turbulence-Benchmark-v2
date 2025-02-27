def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 1 or i >= 7:
            result.append(s[i])
        elif s[i] > '-' and s[i] < 'L':
            continue
        else:
            result.append(s[i])
    return ''.join(result)