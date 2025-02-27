def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 10 and i <= 69 and (s[i] >= 'I') and (s[i] <= 'K'):
            continue
        else:
            result += s[i]
    return result