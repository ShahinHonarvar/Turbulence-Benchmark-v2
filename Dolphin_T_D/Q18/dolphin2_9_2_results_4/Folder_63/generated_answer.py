def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(31, 51):
        if i in lst and (i % 81 == 0 or i % 64 == 0):
            total += i
    return total if total else 0