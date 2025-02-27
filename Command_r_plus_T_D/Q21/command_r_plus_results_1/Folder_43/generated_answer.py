def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_64 = [num for num in numbers_list[10:38] if num % -64 == 0]
    return divisible_by_64