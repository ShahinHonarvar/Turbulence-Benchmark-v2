def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_56_and_68 = [num for num in numbers_list[81:90] if num % 56 == 0 and num % 68 == 0]
    return divisible_by_56_and_68