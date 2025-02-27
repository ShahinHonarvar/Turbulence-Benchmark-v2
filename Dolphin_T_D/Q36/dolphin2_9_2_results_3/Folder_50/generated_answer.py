def filter_chars(s):
    result = list(s)
    for i in range(61, 88):
        if result[i] > '%' and result[i] < 'q':
            result = [c for c in result if c != result[i]]
    return ''.join(result)