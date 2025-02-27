def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisible_by_both = [i for i in lst[8:10] if i % -3 == 0 and i % 6 == 0]
    return divisible_by_both