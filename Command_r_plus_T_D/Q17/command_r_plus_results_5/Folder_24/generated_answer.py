def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for index, num in enumerate(numbers_list[29:54], start=29):
        if num % -68 == 0 and num % -85 == 0:
            divisible_by_both.append(num)
    return divisible_by_both