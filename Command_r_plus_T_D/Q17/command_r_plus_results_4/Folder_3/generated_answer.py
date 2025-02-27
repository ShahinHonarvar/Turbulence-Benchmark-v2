def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisible_by_both = [i for i in lst[38:53] if i % 41 == 0 and i % 47 == 0]
    return divisible_by_both