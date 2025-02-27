def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    div_by_both = [num for num in int_list[30:201] if num % 115 == 0 and num % -115 == 0]
    return div_by_both