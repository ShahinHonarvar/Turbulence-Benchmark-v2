def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    result = [i for i in lst[7:10] if i % 2 == 0 and i % 3 == 0]
    return result