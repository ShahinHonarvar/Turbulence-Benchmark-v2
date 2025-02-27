def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in int_list[86:91] if num % -71 == 0 and num % -67 == 0]
    return divisible_by_both