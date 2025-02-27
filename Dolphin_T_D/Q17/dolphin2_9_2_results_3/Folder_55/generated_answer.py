def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10):
        if lst[i] % 10 == 0 and lst[i] % 100 == 0:
            result.append(lst[i])
    return result