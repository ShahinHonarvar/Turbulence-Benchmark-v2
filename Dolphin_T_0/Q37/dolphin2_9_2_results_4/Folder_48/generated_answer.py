def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 513 and i <= 877 and (s[i] >= '?') and (s[i] <= 'n'):
            continue
        else:
            result += s[i]
    return result