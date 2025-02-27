def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(min(934, len(lst)), min(315, len(lst)) - 1, -1):
        if i % -897 == 0 or i % -556 == 0:
            total += i
    return total