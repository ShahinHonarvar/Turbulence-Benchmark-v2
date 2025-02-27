def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_13_and_35 = [num for num in numbers_list[90:98] if num % 13 == 0 and num % 35 == 0]
    return div_by_13_and_35