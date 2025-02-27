def find_divisors_in_range(x):
    divisors_in_range = [i for i in range(1, x + 1) if x % i == 0 and 6 <= i <= 8]
    return divisors_in_range