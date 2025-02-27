def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_10_and_1000 = [num for num in numbers_list[80:201] if num % 10 == 0 and num % 1000 == 0]
    return divisible_by_10_and_1000