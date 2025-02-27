def sum_of_divisors_in_range(x):
    return sum([i for i in range(48, 61) if x % i == 0])