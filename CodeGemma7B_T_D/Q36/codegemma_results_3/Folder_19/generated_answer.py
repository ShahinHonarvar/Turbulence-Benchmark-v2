def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i >= 77 and i <= 87 and (str[i] > ';') and (str[i] < 'r'):
            continue
        else:
            filtered_str += str[i]
    return filtered_str