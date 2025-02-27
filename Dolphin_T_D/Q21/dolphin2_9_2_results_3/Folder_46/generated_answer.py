def all_ints_div_by_num(lst):
    target_num = 46
    indices = range(21, 98)
    divisible_nums = [num for num in lst[indices] if num % target_num == 0]
    return divisible_nums