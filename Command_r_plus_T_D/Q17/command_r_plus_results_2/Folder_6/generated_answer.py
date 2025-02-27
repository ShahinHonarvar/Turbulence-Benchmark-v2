def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_82_and_90 = [num for num in numbers_list[41:57] if num % 82 == 0 and num % 90 == 0]
    return divisible_by_82_and_90