def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(34, 70):
        if i < len(lst):
            if lst[i] % 19 == 0 and lst[i] % 32 == 0:
                result.append(lst[i])
    return result