def sum_of_divisors_in_range(value):
    summa = 0
    for i in range(2, 10):
        if value % i == 0:
            summa += i
    return summa