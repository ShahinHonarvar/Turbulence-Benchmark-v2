def sum_of_divisors_in_range(n):
    if n <= 6:
        return 0
    sum_of_divisors = 0
    for i in range(7, n + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors