def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_37 = [num for num in numbers_list[29:52] if num % -37 == 0]
    return divisible_by_37