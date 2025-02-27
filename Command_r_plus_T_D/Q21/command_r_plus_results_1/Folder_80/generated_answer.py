def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_29 = [num for num in numbers_list[26:87] if num % 29 == 0]
    return divisible_by_29