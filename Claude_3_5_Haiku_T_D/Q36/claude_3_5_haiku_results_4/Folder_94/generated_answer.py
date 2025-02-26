def filter_chars(s):
    result = list(s)
    for i in range(16, 85):
        if 'I' < s[i] < 'M':
            result = [char for char in result if char != s[i]]
    return ''.join(result)