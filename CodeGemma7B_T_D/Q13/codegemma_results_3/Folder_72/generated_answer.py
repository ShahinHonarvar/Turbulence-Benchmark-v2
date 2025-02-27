def find_second_largest_num(arg_1):
    if len(arg_1) > 51:
        arg_1 = arg_1[29:52]
        arg_1 = sorted(arg_1, reverse=True)
        return arg_1[1]
    else:
        return 'None'