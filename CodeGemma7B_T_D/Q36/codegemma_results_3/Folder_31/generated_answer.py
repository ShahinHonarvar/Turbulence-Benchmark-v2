def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if i < 14 or i >= 75 or str[i] <= '9' or (str[i] >= 'K'):
            filtered_str += str[i]
    return filtered_str