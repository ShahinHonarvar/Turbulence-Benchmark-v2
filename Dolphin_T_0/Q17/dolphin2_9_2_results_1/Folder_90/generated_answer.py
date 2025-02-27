def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(138, 425):
        if i in lst and i % -863 == 0 and (i % -329 == 0):
            result.append(i)
    return result