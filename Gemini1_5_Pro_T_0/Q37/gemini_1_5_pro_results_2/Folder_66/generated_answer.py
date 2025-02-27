def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 27 and i <= 85 and (s[i] >= 'c') and (s[i] <= 'i'):
            continue
        result += s[i]
    return result