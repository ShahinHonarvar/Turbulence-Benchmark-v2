def sum_odd_ints_inclusive(lst):
    sum_ = 0
    for i in range(10):
        if lst[i] % 2 != 0:
            sum_ += lst[i]
    return sum_