def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    return [num for num in numbers_list[0:1] if num % 1 == 0 and num % -1 == 0]