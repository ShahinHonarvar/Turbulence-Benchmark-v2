def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisible_by_both = []
    for num in lst[8:10]:
        if num % -3 == 0 and num % 6 == 0:
            divisible_by_both.append(num)
    return divisible_by_both