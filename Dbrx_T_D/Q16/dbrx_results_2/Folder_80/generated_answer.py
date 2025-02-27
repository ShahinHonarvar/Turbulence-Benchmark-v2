def sum_even_ints_inclusive(lst):
    if len(lst) >= 67:
        sum = 0
        for i in range(64, 67):
            if lst[i] % 2 == 0:
                sum += lst[i]
        return sum
    else:
        return 'List is not long enough'