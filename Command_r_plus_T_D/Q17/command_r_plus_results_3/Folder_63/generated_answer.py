def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_81_and_64 = [num for num in numbers_list[31:51] if num % 81 == 0 and num % 64 == 0]
    return divisible_by_81_and_64