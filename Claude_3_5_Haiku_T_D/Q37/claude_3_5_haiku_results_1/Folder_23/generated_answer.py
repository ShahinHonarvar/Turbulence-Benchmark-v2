def filter_chars(s):
    result = list(s)
    for i in range(51, 78):
        if i < len(s) and 'V' <= s[i] <= 'Y':
            result = [char for char in result if char != s[i]]
    return ''.join(result)