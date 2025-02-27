def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_10_and_100 = []
    for index, num in enumerate(numbers_list[10:101], start=10):
        if num % 10 == 0 and num % 100 == 0:
            divisible_by_both_10_and_100.append(num)
    return divisible_by_both_10_and_100