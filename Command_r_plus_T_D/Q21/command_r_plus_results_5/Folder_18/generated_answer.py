def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_80 = [num for num in numbers_list[26:75] if num % 80 == 0]
    return divisible_by_80