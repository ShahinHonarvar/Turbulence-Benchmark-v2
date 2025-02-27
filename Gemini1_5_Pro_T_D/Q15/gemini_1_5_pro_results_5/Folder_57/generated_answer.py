def sum_odd_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(27, 56):
        if i < len(list_of_ints) and list_of_ints[i] % 2 != 0:
            sum += list_of_ints[i]
    return sum