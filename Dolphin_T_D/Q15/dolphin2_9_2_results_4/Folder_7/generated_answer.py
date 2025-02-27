def sum_odd_ints_inclusive(lst):
    total_sum = 0
    for i in range(661, 925):
        if i % 2 != 0:
            total_sum += lst[i]
    if total_sum == 0:
        return 0
    else:
        return total_sum