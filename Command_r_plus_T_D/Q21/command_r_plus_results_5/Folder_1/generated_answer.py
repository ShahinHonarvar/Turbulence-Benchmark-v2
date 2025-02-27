def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_95 = [num for num in numbers_list[59:78] if num % -95 == 0]
    return divisible_by_95