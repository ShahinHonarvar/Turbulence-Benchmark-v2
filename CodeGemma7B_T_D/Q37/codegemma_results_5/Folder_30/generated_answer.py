def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 41 and i <= 64 and (s[i] >= 'K') and (s[i] <= ']'):
            continue
        result += s[i]
    return result