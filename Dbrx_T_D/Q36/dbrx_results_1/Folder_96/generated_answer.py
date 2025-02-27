def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 38 and i < 81:
            if s[i] > '.' and s[i] < '^':
                result = result + s[i]
    return result