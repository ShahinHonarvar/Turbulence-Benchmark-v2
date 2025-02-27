def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_7 = [num for num in numbers_list[8:9] if num % -7 == 0]
    return divisible_by_7