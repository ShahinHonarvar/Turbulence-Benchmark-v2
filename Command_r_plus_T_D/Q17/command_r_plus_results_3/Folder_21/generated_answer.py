def all_ints_div_by_both_two_nums(lst):
    divisor_1 = -897
    divisor_2 = -556
    start_index = 315
    end_index = 934
    divisible_by_both = []
    for i in range(start_index, end_index + 1):
        if i % divisor_1 == 0 and i % divisor_2 == 0:
            divisible_by_both.append(i)
    return divisible_by_both