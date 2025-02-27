def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 33 < i < 36 and s[i] > '>' and (s[i] < 'A'):
            result += s.replace(s[i], '')
            break
        else:
            result += s[i]
    return result