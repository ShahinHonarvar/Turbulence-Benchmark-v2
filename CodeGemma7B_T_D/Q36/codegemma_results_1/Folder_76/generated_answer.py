def filter_chars(str):
    filtered_string = ''
    for i in range(len(str)):
        if i < 669 or i >= 888 or str[i] < 'B' or (str[i] >= 'Y'):
            filtered_string += str[i]
    return filtered_string