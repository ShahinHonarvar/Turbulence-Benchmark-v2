def sum_of_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Number must be positive.')
    divisors = [i for i in range(3, 10) if num % i == 0]
    return sum(divisors) if divisors else 0