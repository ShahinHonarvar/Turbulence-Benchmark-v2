def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(299, 383):
        if i % 858 == 0 or i % 952 == 0:
            total += lst[i]
    return total