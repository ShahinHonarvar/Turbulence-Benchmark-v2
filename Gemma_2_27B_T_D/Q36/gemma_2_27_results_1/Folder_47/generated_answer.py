def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 45 or i >= 57:
            result.append(s[i])
        elif s[i] > 'F' and s[i] < 'n':
            continue
        else:
            result.append(s[i])
    return ''.join(result)