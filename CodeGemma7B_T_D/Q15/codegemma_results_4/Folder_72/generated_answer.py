def sum_odd_ints_inclusive(lst):
    try:
        sum = 0
        for i in range(29, 52):
            if lst[i] % 2 != 0:
                sum += lst[i]
        return sum
    except IndexError:
        return 0