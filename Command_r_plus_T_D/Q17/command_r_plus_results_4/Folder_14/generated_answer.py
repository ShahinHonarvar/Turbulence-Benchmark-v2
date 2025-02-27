def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    filtered_lst = [num for num in lst[7:10] if num % 2 == 0 and num % 3 == 0]
    return filtered_lst