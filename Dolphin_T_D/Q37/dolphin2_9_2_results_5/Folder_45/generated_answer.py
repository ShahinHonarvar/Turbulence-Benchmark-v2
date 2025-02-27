def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 72 or i > 94 or (not (s[i] >= '.' and s[i] <= 'b')):
            result += s[i]
    return result