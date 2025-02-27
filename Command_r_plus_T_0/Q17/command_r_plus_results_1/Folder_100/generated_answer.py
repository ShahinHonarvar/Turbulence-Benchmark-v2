def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in numbers_list[72:94] if num % 32 == 0 and num % 44 == 0]
    return divisible_by_both