def sum_even_ints_inclusive(lst):
    sum_ = 0
    for i in range(40, 42):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_ += lst[i]
    return sum_