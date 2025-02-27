def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(240, 902):
        if int_list[i] % 546 == 0 and int_list[i] % 709 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both