def sum_odd_ints_inclusive(lst):
    if len(lst) < 924:
        return 'Input list is too short'
    sum = 0
    for i in range(661, 925):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum