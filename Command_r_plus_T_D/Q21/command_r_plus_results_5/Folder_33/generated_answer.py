def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_numbers = [num for num in numbers_list[319:613] if num % -215 == 0]
    return divisible_numbers