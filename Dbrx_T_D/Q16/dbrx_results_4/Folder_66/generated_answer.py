def sum_even_ints_inclusive(lst):
    if len(lst) < 55:
        return 0
    else:
        sum = 0
        for i in range(50, 55):
            if lst[i] % 2 == 0:
                sum += lst[i]
        return sum