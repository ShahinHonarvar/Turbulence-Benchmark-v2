def filter_chars(s):
    result = list(s)
    for i in range(29, min(80, len(s))):
        if 'K' <= s[i] <= 'z':
            result = [char for char in result if char != s[i]]
    return ''.join(result)