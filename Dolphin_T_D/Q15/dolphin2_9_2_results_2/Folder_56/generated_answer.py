def sum_odd_ints_inclusive(lst_ints):
    odd_sum = 0
    for i in range(len(lst_ints)):
        if lst_ints[i] % 2 == 1:
            odd_sum += lst_ints[i]
    return odd_sum