def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if (i >= 171 and i <= 636) and (str[i] > 'c' and str[i] < 's'):
            continue
        filtered_str += str[i]
    return filtered_str