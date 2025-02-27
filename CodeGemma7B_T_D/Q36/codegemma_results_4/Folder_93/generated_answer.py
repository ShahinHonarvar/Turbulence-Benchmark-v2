def filter_chars(str_arg):
    str_list = list(str_arg)
    start_index = 52
    stop_index = 88
    for i in range(start_index, stop_index):
        if str_list[i] > '&' and str_list[i] < 'c':
            str_list.remove(str_list[i])
    return ''.join(str_list)