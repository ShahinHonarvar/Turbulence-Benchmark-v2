def sum_even_ints_inclusive(list_integers):
    sum_even_ints = 0
    for i in range(90, 201):
        if i in list_integers and i % 2 == 0:
            sum_even_ints += i
    return sum_even_ints