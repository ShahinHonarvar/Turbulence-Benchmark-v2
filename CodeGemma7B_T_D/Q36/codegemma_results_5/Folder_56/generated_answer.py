def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 31 and i <= 49 and (s[i] > '/') and (s[i] < 'J'):
            pass
        else:
            result += s[i]
    return result