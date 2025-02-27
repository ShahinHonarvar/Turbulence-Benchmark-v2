def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_71 = [num for num in numbers_list[40:200] if num % 71 != 0]
    return not_divisible_by_71