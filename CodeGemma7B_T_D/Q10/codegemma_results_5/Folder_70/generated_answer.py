def all_odd_ints_exclusive(lst):
    range_lst = lst[38:81]
    odd_nums = [num for num in range_lst if num % 2 != 0]
    return odd_nums if odd_nums else []