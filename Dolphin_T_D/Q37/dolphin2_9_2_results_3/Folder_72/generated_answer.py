def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 35 and i <= 51 and (s[i] >= 'H') and (s[i] <= 's'):
            continue
        else:
            result += s[i]
    return result