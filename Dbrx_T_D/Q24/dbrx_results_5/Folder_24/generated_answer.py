def sum_of_divisors_in_range(n):
    divisors = {i for i in range(1, n + 1) if n % i == 0}
    divisors_in_range = [div for div in divisors if div >= 43 and div <= 95]
    return sum(divisors_in_range)