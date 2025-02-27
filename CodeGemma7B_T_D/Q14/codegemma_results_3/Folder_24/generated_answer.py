def find_second_smallest_num(list_arg):
    if len(list_arg) < 24:
        return 'None'
    list_arg.sort()
    return list_arg[23]