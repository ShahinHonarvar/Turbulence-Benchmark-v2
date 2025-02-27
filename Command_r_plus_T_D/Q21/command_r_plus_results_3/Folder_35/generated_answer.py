def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_57 = [num for num in numbers_list[26:91] if num % 57 == 0]
    return divisible_by_57