def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 25 and i <= 97 and (s[i] >= 'm') and (s[i] <= 'w'):
            continue
        else:
            result += s[i]
    return result