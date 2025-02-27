def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    result = [num for num in lst[51:77] if num % -90 == 0 and num % -59 == 0]
    return result