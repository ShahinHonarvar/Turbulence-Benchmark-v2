def filter_chars(s):
    result = list(s)
    for i in range(33, 61):
        if '3' < s[i] < 'D':
            char = s[i]
            result = [x for x in result if x != char]
    return ''.join(result)