def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[17:53]
    result = []
    for num in range_lst:
        if num % 15 == 0 and num % 57 == 0:
            result.append(num)
    return result