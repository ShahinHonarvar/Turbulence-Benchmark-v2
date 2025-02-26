def filter_chars(s):
    result = list(s)
    for i in range(11, 79):
        if '?' < s[i] < 'm':
            char = s[i]
            result = [x for x in result if x != char]
    return ''.join(result)