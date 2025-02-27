def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-649, -461)
    divisible_by_both = []
    for i in range(828, 933):
        if int_list[i] % divisor_1 == 0 and int_list[i] % divisor_2 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both