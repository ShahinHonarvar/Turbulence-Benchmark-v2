def filter_chars(str_arg):
    filtered_str = ''
    for i in range(len(str_arg)):
        if 41 <= i <= 64 and str_arg[i] >= 'K' and (str_arg[i] <= ']'):
            continue
        filtered_str += str_arg[i]
    return filtered_str