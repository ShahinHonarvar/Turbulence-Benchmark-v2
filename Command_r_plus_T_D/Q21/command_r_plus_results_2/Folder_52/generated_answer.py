def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_46 = [num for num in numbers_list[42:98] if num % 46 == 0]
    return divisible_by_46