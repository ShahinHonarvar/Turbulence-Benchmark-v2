def filter_chars(s):
    result = list(s)
    for i in range(15, 75):
        if '9' < s[i] < 'K':
            result = [char for char in result if char != s[i]]
    return ''.join(result)