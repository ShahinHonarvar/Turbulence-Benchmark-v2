def sum_of_divisors_in_range(n):
    if n < 3:
        return 0
    divisors = [i for i in range(3, 8) if n % i == 0]
    return sum(divisors)