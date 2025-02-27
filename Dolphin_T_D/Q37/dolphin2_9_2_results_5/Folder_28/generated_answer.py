def filter_chars(s):
    result = list(s)
    for i in range(20, 80):
        if i >= 33 and i <= 84:
            result = [c for c in result if c != result[i]]
    return ''.join(result)