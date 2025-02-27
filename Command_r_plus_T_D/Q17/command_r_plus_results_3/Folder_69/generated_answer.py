def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = [num for num in numbers_list[61:89] if num % 31 == 0 and num % 11 == 0]
    return divisible_by_both