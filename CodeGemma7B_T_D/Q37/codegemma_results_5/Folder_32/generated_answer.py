def filter_chars(str_i):
    filtered_string = ''
    for i in range(len(str_i)):
        if i >= 23 and i <= 89 and (str_i[i] >= 'w') and (str_i[i] <= '{'):
            filtered_string += ''
        else:
            filtered_string += str_i[i]
    return filtered_string