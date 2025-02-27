def sum_even_ints_inclusive(list):
    sum = 0
    for index in range(27, 56):
        if list[index] % 2 == 0:
            sum += list[index]
    return sum if sum else 0