def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(max(0, min(len(lst) - 1, 56)), min(len(lst), 83)):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum