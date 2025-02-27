def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 80):
        if i < 0:
            i = -i
        if lst[i] % -74 == 0 and lst[i] % -58 == 0:
            result.append(lst[i])
    return result