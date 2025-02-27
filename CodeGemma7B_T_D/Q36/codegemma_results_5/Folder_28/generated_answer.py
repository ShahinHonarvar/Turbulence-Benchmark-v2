def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i < 31 or i >= 73:
            filtered_str += str[i]
        elif str[i] > 'M' and str[i] < 'j':
            continue
        else:
            filtered_str += str[i]
    return filtered_str