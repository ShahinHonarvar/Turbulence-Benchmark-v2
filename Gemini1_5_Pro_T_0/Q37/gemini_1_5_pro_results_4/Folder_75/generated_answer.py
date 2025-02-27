def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (i >= 34 and i <= 67 and (c >= 'W') and (c <= 'x')):
            result += c
    return result