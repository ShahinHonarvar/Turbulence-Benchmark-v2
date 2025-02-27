def sum_even_ints_inclusive(lst):
    sum_ = 0
    for i in range(246, 751):
        if i % 2 == 0:
            sum_ += lst[i]
    return sum_