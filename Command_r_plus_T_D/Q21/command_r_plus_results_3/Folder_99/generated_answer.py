def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_763 = [num for num in numbers_list[160:971] if num % 763 == 0]
    return divisible_by_763