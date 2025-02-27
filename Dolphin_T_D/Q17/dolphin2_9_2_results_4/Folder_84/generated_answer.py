def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(78, 82):
        if i in lst and lst[i] % 240 == 0:
            result.append(lst[i])
    return result