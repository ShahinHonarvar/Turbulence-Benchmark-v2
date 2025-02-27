def all_ints_div_by_both_two_nums(num_list):
    divisible = []
    for num in num_list[93:95]:
        if num % -53 == 0 and num % -91 == 0:
            divisible.append(num)
    return divisible