def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    return [num for num in lst[3:10] if num % 6 == 0 and num % 1 == 0]