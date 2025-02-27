def sum_even_ints_inclusive(list_ints):
    even_sum = 0
    for i in range(686, 988):
        if i % 2 == 0 and i < len(list_ints) and (list_ints[i] % 2 == 0):
            even_sum += list_ints[i]
    return even_sum