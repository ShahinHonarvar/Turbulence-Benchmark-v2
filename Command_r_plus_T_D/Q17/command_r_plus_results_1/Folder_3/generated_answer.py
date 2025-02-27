def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(38, 53):
        if int_list[i] % -41 == 0 and int_list[i] % -47 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both