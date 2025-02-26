def filter_chars(s):
    result = list(s)
    for i in range(43, 78):
        if '!' < s[i] < '?':
            result = [char for char in result if char != s[i]]
    return ''.join(result)