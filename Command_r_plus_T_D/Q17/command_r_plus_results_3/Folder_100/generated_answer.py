def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    result = [int_val for int_val in int_list[72:94] if int_val % 32 == 0 and int_val % 44 == 0]
    return result