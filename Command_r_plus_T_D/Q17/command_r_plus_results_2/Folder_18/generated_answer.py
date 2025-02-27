def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[55:67] if num % 22 == 0 and num % 82 == 0]
    return result