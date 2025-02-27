def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for index, num in enumerate(numbers_list[50:93], start=50):
        if num % -94 == 0 and num % -95 == 0:
            divisible_by_both.append(num)
    return divisible_by_both