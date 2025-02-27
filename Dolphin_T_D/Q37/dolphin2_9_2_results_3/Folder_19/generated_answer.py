def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 35 and i <= 89 and (s[i] >= 'E') and (s[i] <= 't'):
            continue
        result += s[i]
    return result