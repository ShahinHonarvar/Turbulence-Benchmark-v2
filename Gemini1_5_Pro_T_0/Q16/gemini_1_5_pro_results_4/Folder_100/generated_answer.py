def sum_even_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(max(0, min(42, len(list_of_ints) - 1)), min(68, len(list_of_ints) - 1) + 1):
        if list_of_ints[i] % 2 == 0:
            sum += list_of_ints[i]
    return sum