def find_divisors_in_range(n):
    divisors = [x for x in range(1, n + 1) if n % x == 0]
    return [i for i in divisors if i >= 58 and i <= 90]