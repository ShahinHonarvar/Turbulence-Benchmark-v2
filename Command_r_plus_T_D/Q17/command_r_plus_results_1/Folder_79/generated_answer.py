def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in numbers_list[8:10] if num % -3 == 0 and num % 6 == 0]
    return divisible_by_both