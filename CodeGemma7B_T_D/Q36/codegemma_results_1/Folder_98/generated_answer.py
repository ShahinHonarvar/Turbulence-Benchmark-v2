def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i < 4 or i >= 8:
            filtered_str += str[i]
    return filtered_str