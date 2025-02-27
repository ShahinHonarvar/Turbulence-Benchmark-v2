def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_91 = [num for num in numbers_list[33:36] if num % 91 == 0]
    return divisible_by_91