def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(max(527, 0), min(539, len(lst))):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum