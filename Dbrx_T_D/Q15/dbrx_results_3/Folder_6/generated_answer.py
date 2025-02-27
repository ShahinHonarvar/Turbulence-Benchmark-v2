def sum_odd_ints_inclusive(lst):
    if len(lst) < 67:
        return 'List is not long enough.'
    else:
        sum = 0
        for i in range(10, 67):
            if lst[i] % 2 != 0:
                sum += lst[i]
        return sum