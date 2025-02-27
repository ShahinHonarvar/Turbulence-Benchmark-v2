def filter_chars(str):
    filtered_str = ''
    for i in range(948):
        if i < 476 or (i > 475 and str[i] <= 'b' or str[i] >= 'd'):
            filtered_str += str[i]
    return filtered_str