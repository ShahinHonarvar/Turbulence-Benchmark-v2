def filter_chars(str1):
    filtered_str = ''
    for i in range(len(str1)):
        if i >= 27 and i <= 29 and (str1[i] >= ';') and (str1[i] <= 'b'):
            continue
        filtered_str += str1[i]
    return filtered_str