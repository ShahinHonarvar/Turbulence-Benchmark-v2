def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if not (24 <= i <= 79 and (str[i] >= 'a' and str[i] <= 'f')):
            filtered_str += str[i]
    return filtered_str