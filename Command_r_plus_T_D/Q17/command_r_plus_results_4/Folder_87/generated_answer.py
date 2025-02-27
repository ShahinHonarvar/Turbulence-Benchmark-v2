def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[18:53] if num % 15 == 0 and num % 57 == 0]
    return result