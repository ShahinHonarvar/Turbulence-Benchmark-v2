def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_10_and_100 = [num for num in numbers_list[10:101] if num % 10 == 0 and num % 100 == 0]
    return divisible_by_10_and_100