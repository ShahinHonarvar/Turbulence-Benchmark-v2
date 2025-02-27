def all_ints_div_by_both_two_nums(input_list):
    divisible_numbers = []
    for i in range(13, 92):
        if input_list[i] % -65 == 0 and input_list[i] % -62 == 0:
            divisible_numbers.append(input_list[i])
    return divisible_numbers