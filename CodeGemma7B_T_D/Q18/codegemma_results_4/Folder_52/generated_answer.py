def sum_ints_div_by_either_nums(lst):
    sum1 = sum([i for i in lst[48:60] if i % 88 == 0])
    sum2 = sum([i for i in lst[48:60] if i % 58 == 0])
    if not (sum1 or sum2):
        return 0
    return sum1 + sum2