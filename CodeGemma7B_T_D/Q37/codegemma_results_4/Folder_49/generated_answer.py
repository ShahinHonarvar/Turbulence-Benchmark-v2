def filter_chars(str):
    filtered_str = ''
    for i in range(len(str)):
        if not (str[i] >= '*' and str[i] <= 'b' and (i >= 42) and (i <= 97)):
            filtered_str += str[i]
    return filtered_str