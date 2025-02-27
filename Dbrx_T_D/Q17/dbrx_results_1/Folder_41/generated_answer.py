def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(min(9, len(lst))):
        if lst[i] % 6 == 0 and lst[i] % -3 == 0:
            result.append(lst[i])
    return result