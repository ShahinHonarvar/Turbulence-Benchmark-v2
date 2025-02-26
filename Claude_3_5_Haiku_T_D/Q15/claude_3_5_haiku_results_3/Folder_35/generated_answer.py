def sum_odd_ints_inclusive(lst):
    if len(lst) <= 48:
        return 0
    odd_sum = 0
    for num in lst[30:49]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum