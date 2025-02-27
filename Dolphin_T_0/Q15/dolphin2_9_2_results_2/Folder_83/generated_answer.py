def sum_odd_ints_inclusive(lst):
    if not lst:
        return 0
    sum = 0
    for i in range(90, 201):
        if i < len(lst) and lst[i] % 2 != 0:
            sum += lst[i]
    return sum