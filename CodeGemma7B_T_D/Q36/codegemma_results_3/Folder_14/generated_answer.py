def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i < 41 or i > 56:
            filtered_str += str[i]
        elif str[i] > 'Z' and str[i] < 'c':
            pass
        else:
            filtered_str += str[i]
    return filtered_str