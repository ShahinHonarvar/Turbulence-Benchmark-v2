def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_11 = [num for i, num in enumerate(numbers_list[10:111], 11) if num % 11 == 0]
    return divisible_by_11