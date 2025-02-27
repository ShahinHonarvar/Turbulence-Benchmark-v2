def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i > 27 and i < 75 and (s[i] > 'A') and (s[i] < 'i'):
            continue
        else:
            result += s[i]
    return result