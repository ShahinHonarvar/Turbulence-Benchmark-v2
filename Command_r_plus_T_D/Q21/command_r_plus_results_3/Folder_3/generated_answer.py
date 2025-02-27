def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_numbers = [num for i, num in enumerate(numbers_list[25:60]) if num % -26 == 0]
    return divisible_numbers