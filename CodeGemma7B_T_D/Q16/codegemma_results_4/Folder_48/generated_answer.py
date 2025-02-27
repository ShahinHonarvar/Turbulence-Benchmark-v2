def sum_even_ints_inclusive(lst):
    sum_of_evens = 0
    for i in range(533, 606):
        if lst[i] % 2 == 0:
            sum_of_evens += lst[i]
    if sum_of_evens == 0:
        return 0
    else:
        return sum_of_evens