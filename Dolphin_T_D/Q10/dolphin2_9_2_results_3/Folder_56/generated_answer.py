def all_odd_ints_exclusive(integers):
    odd_integers = []
    if len(integers) > 9:
        for i in range(7, 9):
            if integers[i] % 2 != 0:
                odd_integers.append(integers[i])
    return odd_integers