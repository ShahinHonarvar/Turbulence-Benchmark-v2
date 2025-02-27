def sum_even_ints_inclusive(array):
    sum = 0
    if len(array) >= 7 and array[6] % 2 == 0:
        return array[6]
    else:
        return 0