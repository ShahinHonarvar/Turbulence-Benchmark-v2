def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or not isinstance(n, positive):
        raise TypeError('n must be a positive integer')
    sum_of_divisors = 0
    for i in range(20, 51):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors if sum_of_divisors else 0