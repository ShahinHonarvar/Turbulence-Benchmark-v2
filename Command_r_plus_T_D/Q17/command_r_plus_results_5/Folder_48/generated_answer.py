def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in numbers_list[306:958] if num % 982 == 0 and num % 319 == 0]
    return divisible_by_both