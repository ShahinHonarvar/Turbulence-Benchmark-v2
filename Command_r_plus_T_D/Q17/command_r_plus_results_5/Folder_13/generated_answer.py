def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    div_by_45_and_20 = [i for i in lst[13:19] if i % 45 == 0 and i % 20 == 0]
    return div_by_45_and_20