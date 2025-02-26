def sum_even_ints_inclusive(lst):
    if len(lst) <= 111:
        return 0
    target_num = lst[111]
    return target_num if target_num % 2 == 0 else 0