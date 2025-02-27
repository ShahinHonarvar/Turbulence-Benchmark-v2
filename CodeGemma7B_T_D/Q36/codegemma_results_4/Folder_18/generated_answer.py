def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i >= 587 and i <= 648 and (str[i] > ',') and (str[i] < 'c'):
            continue
        filtered_str += str[i]
    return filtered_str