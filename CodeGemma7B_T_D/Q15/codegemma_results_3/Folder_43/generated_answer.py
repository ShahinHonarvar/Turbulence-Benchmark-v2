def sum_odd_ints_inclusive(lst):
    count = 0
    sum = 0
    for i in range(68, 87):
        if lst[i] % 2 == 1:
            count += 1
            sum += lst[i]
    if count == 0:
        return 0
    else:
        return sum