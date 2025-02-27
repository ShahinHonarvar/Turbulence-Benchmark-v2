def all_ints_div_by_num(num_list):
    res = [num for num in range(13, 69) if num in num_list and num % 71 == 0]
    return res or []