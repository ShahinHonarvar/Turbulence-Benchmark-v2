def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_31 = [num for i, num in enumerate(numbers_list) if num % -31 != 0 and 90 <= i < 200]
    return not_divisible_by_31