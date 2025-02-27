def all_odd_ints_exclusive(num_list):
    odd_nums = [num for num in num_list[10:76] if num % 2 != 0]
    return odd_nums if odd_nums else []