def sum_even_ints_inclusive(list_of_integers):
    sum_ = 0
    for i in range(8, 10):
        if list_of_integers[i] % 2 == 0:
            sum_ += list_of_integers[i]
    return sum_