def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_28 = [int for int in int_list[36:41] if int % 28 == 0]
    return divisible_by_28