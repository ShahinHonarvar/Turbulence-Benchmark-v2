def sum_of_divisors_in_range(n):
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 83 <= i <= 95:
            sum_divisors += i
    return sum_divisors