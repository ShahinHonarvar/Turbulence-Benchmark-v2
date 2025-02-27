def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    div_by_both = [i for i in lst[42:88] if i % 90 == 0 and i % 74 == 0]
    return div_by_both