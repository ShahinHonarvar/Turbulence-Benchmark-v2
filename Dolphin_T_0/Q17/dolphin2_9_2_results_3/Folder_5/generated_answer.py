def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] % 6 == 0 and lst[i] % 4 == 0:
            result.append(lst[i])
    return result