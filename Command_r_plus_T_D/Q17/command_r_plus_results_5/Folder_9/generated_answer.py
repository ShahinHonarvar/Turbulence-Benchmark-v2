def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    return [num for num in lst[70:201] if num % 3 == 0 and num % -300 == 0]