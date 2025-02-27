def sum_even_ints_inclusive(lst):
    sum_even = 0
    range_start = 0
    range_end = 9
    if not lst:
        return 0
    for i in range(range_start, range_end + 1):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even