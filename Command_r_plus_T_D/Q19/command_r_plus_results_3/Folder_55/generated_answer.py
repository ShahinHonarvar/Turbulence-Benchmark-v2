def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    non_divisible_by_10 = [num for i, num in enumerate(numbers_list) if num % 10 != 0 and 0 < i < 9]
    return non_divisible_by_10