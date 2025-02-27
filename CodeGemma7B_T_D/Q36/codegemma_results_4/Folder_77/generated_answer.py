def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i not in range(221, 419):
            filtered_str += str[i]
    return filtered_str.replace('-', '')