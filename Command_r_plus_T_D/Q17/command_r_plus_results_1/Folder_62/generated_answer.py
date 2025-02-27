def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_39_and_15 = [num for num in int_list[44:60] if num % 39 == 0 and num % 15 == 0]
    return divisible_by_39_and_15