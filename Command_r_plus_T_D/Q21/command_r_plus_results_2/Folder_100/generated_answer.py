def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_86 = [num for num in numbers_list[86:93] if num % 86 == 0]
    return divisible_by_86