def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(28, 33):
        if i < 0 or i >= len(lst):
            break
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum