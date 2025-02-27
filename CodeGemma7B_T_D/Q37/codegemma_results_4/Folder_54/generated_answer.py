def filter_chars(string):
    filtered_str = ''
    for i in range(len(string)):
        if i >= 46 and i <= 85 and (string[i] >= '-') and (string[i] <= 'X'):
            continue
        filtered_str += string[i]
    return filtered_str