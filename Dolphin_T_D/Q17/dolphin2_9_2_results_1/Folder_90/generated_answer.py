def all_ints_div_by_both_two_nums(lst):
    divisible = []
    for i in range(138, 425):
        if i in lst and i % -863 == 0 and (i % -329 == 0):
            divisible.append(i)
    return divisible