def sum_ints_div_by_either_nums(args_list):
    if len(args_list) <= 200:
        return 0
    else:
        subset_list = args_list[50:201]
        return sum([i for i in subset_list if i % -34 == 0 or i % 64 == 0])