def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(56, 83):
        if i in lst and i % 2 == 0:
            result += i
    return result