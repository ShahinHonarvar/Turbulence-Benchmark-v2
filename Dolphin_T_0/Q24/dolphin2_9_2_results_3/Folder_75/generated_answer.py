def sum_of_divisors_in_range(x):
    return sum((i for i in range(38, 66) if x % i == 0))