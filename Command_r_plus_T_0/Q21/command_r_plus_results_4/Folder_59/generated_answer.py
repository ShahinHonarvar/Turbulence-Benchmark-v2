def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_nine = [num for num in numbers_list if num % 9 == 0]
    return divisible_by_nine[:1]