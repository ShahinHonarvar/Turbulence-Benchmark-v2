def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_22 = [num for num in numbers_list[43:60] if num % 22 == 0]
    return divisible_by_22