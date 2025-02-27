def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(240, min(902, len(lst))):
        if lst[i] % 546 == 0 and lst[i] % 709 == 0:
            result.append(lst[i])
    return result