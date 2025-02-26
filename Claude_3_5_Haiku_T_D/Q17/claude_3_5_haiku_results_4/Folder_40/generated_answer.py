def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 2:
        return []
    first_num = lst[0]
    second_num = lst[1]
    return [num for num in lst if num % first_num == 0 and num % second_num == 0]