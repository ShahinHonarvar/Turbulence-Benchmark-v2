def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return sum(divisors) if all((469 <= i <= 682 for i in divisors)) else 0