def filter_chars(s):
    result = s[:12]
    for i in range(12, min(len(s), 89)):
        if s[i] >= '&' and s[i] <= 'v':
            continue
        else:
            result += s[i]
    return result