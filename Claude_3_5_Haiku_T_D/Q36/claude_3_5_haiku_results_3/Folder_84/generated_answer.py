def filter_chars(s):
    result = list(s)
    for i in range(172, 636):
        if 'c' < result[i] < 's':
            current_char = result[i]
            result = [char for char in result if char != current_char]
    return ''.join(result)