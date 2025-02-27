def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_200 = [num for i, num in enumerate(numbers_list) if i >= 20 and i < 200 and (num % -200 != 0)]
    return not_divisible_by_200