def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 54 or i >= 92:
            result.append(s[i])
        elif 'J' < s[i] < 'X':
            continue
        else:
            result.append(s[i])
    return ''.join(result)