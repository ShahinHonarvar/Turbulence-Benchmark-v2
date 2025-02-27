def sum_odd_ints_inclusive(li):
    return sum((li[i] for i in range(25, 60) if li[i] % 2 != 0))