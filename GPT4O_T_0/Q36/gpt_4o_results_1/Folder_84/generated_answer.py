def filter_chars(s):
    if len(s) <= 171:
        return s
    filtered = s[:172]
    for i in range(172, min(636, len(s))):
        if 'c' < s[i] < 's':
            filtered += s[i + 1:].replace(s[i], '')
        else:
            filtered += s[i]
    if len(s) > 636:
        filtered += s[636:]
    return filtered