def filter_chars(s):
    result = list(s)
    for i in range(59, 82):
        if 'F' < s[i] < 'O':
            result = [char for char in result if char != s[i]]
    return ''.join(result)