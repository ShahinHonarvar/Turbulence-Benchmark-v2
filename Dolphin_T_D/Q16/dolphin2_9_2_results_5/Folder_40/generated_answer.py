def sum_even_ints_inclusive(ints):
    sum = 0
    for i in ints[:3]:
        if i % 2 == 0:
            sum += i
    return sum