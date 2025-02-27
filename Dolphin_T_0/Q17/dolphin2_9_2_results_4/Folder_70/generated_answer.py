def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(42, 44):
        if i < len(lst):
            if lst[i] % 15 == 0 and lst[i] % 87 == 0:
                result.append(lst[i])
    return result