def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_15 = [num for num in int_list[31:68] if num % -15 == 0]
    return divisible_by_15