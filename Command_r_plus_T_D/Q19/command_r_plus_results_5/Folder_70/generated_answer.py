def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_13 = [num for num in numbers_list[90:97] if num % 13 != 0]
    return not_divisible_by_13