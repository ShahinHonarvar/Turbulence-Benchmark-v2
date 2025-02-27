def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i >= 5 and i <= 6 and (str[i] >= 'G') and (str[i] <= 'p'):
            continue
        filtered_str += str[i]
    return filtered_str