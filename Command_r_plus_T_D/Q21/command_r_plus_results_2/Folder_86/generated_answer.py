def all_ints_div_by_num(num_list: list[int]) -> list[int]:
    divisible_by_88 = [num for num in num_list[44:74] if num % 88 == 0]
    return divisible_by_88