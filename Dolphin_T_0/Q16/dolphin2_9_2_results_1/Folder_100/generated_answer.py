def sum_even_ints_inclusive(l):
    sum_ = 0
    for i in range(42, 69):
        if i < len(l) and l[i] % 2 == 0:
            sum_ += l[i]
    return sum_