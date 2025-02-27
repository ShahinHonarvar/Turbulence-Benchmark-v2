def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = [i for i in int_list[46:92] if i % 67 == 0 and i % 15 == 0]
    return divisible_by_both