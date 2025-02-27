def find_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 84 <= i <= 86]
    return divisors