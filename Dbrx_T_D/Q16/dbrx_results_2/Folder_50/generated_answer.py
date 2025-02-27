def sum_even_ints_inclusive(lst):
    if len(lst) < 85:
        return 'List is not long enough. List length: ' + str(len(lst))
    else:
        lst_slice = lst[69:85]
        even_ints = [i for i in lst_slice if i % 2 == 0]
        if even_ints:
            return sum(even_ints)
        else:
            return 0