def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(639, 976):
        if lst[i] % 2 != 0:
            sum += lst[i]
    if sum == 0:
        return 0
    else:
        return sum