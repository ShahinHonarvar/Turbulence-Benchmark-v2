def all_ints_div_by_num(num_list):
    divisible_nums = []
    for num in num_list:
        if num % 5 == 0:
            divisible_nums.append(num)
    return divisible_nums