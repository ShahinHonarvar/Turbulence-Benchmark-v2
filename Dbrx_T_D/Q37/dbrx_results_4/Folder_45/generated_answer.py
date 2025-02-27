def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 72 <= i <= 94:
            char = s[i]
            if s[i] >= '.' and s[i] <= 'b':
                continue
        result += s[i]
    return result