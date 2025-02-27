def sum_odd_ints_inclusive(lst):
    for i in range(len(lst)):
        if i >= 262 and i <= 746:
            if lst[i] % 2 != 0:
                sum += lst[i]
    if sum == 0:
        return 0
    else:
        return sum