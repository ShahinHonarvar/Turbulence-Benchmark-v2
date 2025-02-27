def sum_of_divisors_in_range(n):
    divisors = [i for i in range(max(70, n // 2), min(93, n) + 1) if n % i == 0]
    return sum(divisors)