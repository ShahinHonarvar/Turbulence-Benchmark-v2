def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_77 = [num for num in numbers_list[66:82] if num % 77 == 0]
    return divisible_by_77