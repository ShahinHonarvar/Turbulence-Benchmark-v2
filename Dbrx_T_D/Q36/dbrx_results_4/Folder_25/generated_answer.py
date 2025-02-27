def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 24 or i >= 37:
            result += s[i]
            continue
        if s[i] > 'A' and s[i] < 'h':
            result += s[i]
    return result