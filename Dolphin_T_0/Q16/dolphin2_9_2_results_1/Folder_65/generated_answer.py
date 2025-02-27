def sum_even_ints_inclusive(lst):
    sum_ = 0
    for i in range(56, 99):
        if i < len(lst) and i % 2 == 0:
            sum_ += lst[i]
    return sum_