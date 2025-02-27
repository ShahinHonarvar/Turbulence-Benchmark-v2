def find_divisors_in_range(x):
    divisors = [i for i in range(15, 93) if x % i == 0]
    return divisors