def filter_chars(s):
    result = list(s)
    for i in range(62, 88):
        if '%' < result[i] < 'q':
            char_to_remove = result[i]
            result = [c for c in result if c != char_to_remove]
    return ''.join(result)