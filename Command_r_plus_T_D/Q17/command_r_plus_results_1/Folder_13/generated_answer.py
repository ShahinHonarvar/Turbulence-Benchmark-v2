def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_45_and_20 = [num for num in numbers_list[13:19] if num % 45 == 0 and num % 20 == 0]
    return divisible_by_45_and_20