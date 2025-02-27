def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    div_by_both = [num for num in int_list[10:29] if num % -61 == 0 and num % -64 == 0]
    return div_by_both