def sum_even_ints_inclusive(lst):
    if not lst or len(lst) <= 12:
        return 0
    sum_even = 0
    for i in range(12, min(93, len(lst))):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even