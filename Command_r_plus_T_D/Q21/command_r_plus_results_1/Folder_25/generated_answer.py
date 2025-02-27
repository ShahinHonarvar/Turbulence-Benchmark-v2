def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_97 = [num for num in numbers_list[25:42] if num % -97 == 0]
    return divisible_by_97