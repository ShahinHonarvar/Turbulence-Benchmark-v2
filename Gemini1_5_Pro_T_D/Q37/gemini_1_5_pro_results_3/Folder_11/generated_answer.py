def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i in range(29, 98) and s[i] >= '-' and (s[i] <= 'n'):
            continue
        result += s[i]
    return result