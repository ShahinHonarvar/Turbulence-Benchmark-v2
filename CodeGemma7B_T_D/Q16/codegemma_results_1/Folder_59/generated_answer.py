def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(10):
        if lst[i % len(lst)] % 2 == 0:
            sum += lst[i % len(lst)]
    return sum