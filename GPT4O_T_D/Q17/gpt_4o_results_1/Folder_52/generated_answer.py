def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(48, min(60, len(lst))):
        if lst[i] % 88 == 0 and lst[i] % 58 == 0:
            result.append(lst[i])
    return result