def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    non_divisible_numbers = [num for i, num in enumerate(numbers_list[32:44]) if num % 34 != 0]
    return non_divisible_numbers