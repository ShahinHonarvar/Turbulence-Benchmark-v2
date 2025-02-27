def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    sum_of_divisors = sum((i for i in divisors if 120 <= i <= 349))
    return sum_of_divisors