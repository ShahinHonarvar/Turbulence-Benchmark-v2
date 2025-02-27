def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(min(len(lst), 5)):
        if lst[i] % 8 == 0 and lst[i] % -3 == 0:
            result.append(lst[i])
    return result