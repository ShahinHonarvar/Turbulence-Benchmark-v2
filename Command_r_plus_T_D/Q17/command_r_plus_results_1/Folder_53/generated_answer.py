def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    div_by_both = [i for i in int_list[200:201] if i % 17 == 0 and i % -5 == 0]
    return div_by_both