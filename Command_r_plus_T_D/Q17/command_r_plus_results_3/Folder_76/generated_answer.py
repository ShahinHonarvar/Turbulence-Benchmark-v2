def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[250:630] if num % 850 == 0 and num % 587 == 0]
    return result