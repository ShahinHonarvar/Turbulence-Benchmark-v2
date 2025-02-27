def sum_odd_ints_inclusive(lst):
    if len(lst) < 33 or not isinstance(lst, list):
        return 0
    sum = 0
    for i in range(28, 33):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum