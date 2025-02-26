def filter_chars(s):
    result = list(s)
    for i in range(58, 69):
        if i < len(s) and '(' < s[i] < 'W':
            result = [char for char in result if char != s[i]]
    return ''.join(result)