def sum_even_ints_inclusive(lst):
    sum_of_even = 0
    for i in range(111, 112):
        if lst[i] % 2 == 0:
            sum_of_even += lst[i]
    return sum_of_even