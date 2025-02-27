def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for num in int_list[12:76]:
        if num % -66 == 0 and num % -32 == 0:
            divisible_ints.append(num)
    return divisible_ints