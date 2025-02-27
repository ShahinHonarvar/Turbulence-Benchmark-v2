def filter_chars(s):
    result = ''
    if len(s) >= 877:
        for i in range(513, 878):
            if s[i] >= '?' and s[i] <= 'n':
                continue
            result += s[i]
    return result