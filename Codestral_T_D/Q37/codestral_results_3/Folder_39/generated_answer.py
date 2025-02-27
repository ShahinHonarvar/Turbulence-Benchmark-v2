def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 52 and i <= 81 and (s[i] >= 'A') and (s[i] <= 'U'):
            continue
        result += s[i]
    return result