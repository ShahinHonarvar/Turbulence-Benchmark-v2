def sum_of_divisors_in_range(n):
    summ = 0
    for i in range(1, 10):
        if n % i == 0:
            summ += i
    return summ