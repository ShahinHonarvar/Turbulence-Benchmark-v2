def filter_chars(s):
    result = list(s)
    for i in range(73, 93):
        if '<' < s[i] < 'J':
            result = [char for char in result if char != s[i]]
    return ''.join(result)