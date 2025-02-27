def sum_of_divisors_in_range(n):
    divisors = list(range(1, n + 1))
    divisors = [i for i in divisors if n % i == 0 and 3 <= i <= 6]
    return sum(divisors) if divisors else 0