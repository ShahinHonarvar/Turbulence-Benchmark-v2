def sum_odd_ints_inclusive(list_of_ints):
    odd_sum = 0
    for i in range(30, 201):
        if list_of_ints[i] % 2 != 0:
            odd_sum += list_of_ints[i]
    return odd_sum if odd_sum != 0 else 0