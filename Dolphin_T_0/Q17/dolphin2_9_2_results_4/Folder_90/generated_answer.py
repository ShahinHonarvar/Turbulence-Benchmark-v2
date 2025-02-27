def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(138, 425):
        if i % -863 == 0 and i % -329 == 0:
            result.append(lst[i])
    return result