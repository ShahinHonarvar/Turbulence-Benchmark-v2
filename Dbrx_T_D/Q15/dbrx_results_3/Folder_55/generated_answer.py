def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(min(10, len(lst))):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum