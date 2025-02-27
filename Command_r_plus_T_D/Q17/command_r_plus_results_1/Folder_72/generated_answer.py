def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in int_list[38:82] if num % -61 == 0 and num % -71 == 0]
    return divisible_by_both