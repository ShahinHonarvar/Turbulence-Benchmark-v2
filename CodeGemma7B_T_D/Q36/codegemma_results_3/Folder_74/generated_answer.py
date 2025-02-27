def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i >= 33 and i <= 36 and (str[i] > '>') and (str[i] < 'A'):
            continue
        filtered_str += str[i]
    return filtered_str