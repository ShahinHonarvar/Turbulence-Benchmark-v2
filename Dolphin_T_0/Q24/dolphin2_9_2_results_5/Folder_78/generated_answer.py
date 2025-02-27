def sum_of_divisors_in_range(x):
    return sum((i for i in range(20, 51) if x % i == 0))