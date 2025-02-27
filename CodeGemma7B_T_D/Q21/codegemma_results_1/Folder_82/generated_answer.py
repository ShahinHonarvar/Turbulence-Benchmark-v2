def all_ints_div_by_num(num_list):
    if not num_list:
        return []
    divisible_nums = []
    for num in num_list:
        if num >= 0 and num <= 2:
            if num % 3 == 0:
                divisible_nums.append(num)
    if not divisible_nums:
        return []
    return divisible_nums