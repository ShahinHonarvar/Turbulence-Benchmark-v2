def all_ints_div_by_num(int_list):
    divisible_nums = []
    for num in int_list:
        if num % 2 == 0:
            divisible_nums.append(num)
    return divisible_nums