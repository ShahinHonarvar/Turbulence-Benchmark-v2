def find_divisors_in_range(x):
    divisors = [i for i in range(1, x + 1) if x % i == 0]
    return [i for i in set(divisors) if 35 <= i <= 37]