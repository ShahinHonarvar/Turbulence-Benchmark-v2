def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_57 = [num for num in int_list[27:91] if num % 57 == 0]
    return divisible_by_57