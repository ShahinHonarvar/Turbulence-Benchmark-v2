def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_4 = [num for num in numbers_list if num % 4 == 0]
    return divisible_by_4[:1]