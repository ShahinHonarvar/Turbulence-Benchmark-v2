def sum_of_divisors_in_range(num):
    if num < 1:
        return 0
    return sum((i for i in range(1, num + 1) if num % i == 0))