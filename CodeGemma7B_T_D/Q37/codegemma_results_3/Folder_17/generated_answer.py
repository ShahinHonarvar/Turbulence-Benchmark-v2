def filter_chars(str):
    filtered_string = ''
    for i in range(len(str)):
        if i >= 27 and i <= 29 and (str[i] >= ';' and str[i] <= 'b'):
            continue
        else:
            filtered_string += str[i]
    return filtered_string