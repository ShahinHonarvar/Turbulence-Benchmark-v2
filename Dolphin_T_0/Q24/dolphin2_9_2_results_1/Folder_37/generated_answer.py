def sum_of_divisors_in_range(n):
    if 3 > n or n > 7:
        return 0
    sum_divisors = 0
    for i in range(3, n + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors