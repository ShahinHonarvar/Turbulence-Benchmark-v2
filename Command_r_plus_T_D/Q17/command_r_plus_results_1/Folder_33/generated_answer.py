def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for index, num in enumerate(numbers_list[281:695], start=281):
        if num % -722 == 0 and num % -731 == 0:
            divisible_by_both.append(num)
    return divisible_by_both