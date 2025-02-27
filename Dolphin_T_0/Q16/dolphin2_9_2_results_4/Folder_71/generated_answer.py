def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(26, 53):
        if i != 53:
            if lst[i] % 2 == 0:
                sum = sum + lst[i]
    return sum