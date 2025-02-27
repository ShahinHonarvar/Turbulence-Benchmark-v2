def sum_of_divisors_in_range(num):
    return sum((i for i in range(48, 93) if num % i == 0))