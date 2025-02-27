def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(39, 58):
        if n % i == 0 and i != n:
            sum += i
    return sum