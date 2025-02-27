def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_8 = [num for num in numbers_list[0:1] if num % 8 == 0]
    return divisible_by_8