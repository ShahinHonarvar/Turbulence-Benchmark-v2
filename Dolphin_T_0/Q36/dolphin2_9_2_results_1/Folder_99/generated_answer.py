def filter_chars(s):
    result = list(s)
    for i in range(476, 948):
        if 'b' < s[i] < 'd':
            result = [x for x in result if x != s[i] for i in range(476, 948)]
    return ''.join(result)