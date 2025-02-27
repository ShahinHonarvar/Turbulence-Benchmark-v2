def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_86 = [num for num in numbers_list[18:60] if num % 86 != 0]
    return not_divisible_by_86