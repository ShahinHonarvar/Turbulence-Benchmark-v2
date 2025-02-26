def filter_chars(s):
    result = list(s)
    for i in range(343, 665):
        if '%' < s[i] < 'U':
            char = s[i]
            result = [x for x in result if x != char]
    return ''.join(result)