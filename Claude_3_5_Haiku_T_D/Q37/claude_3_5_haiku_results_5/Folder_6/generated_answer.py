def filter_chars(s):
    result = list(s)
    for i in range(13, 29):
        if i < len(s) and 'c' <= s[i] <= 'n':
            result = [char for char in result if char != s[i]]
    return ''.join(result)