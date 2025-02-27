def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    divisors = [i for i in range(6, 8) if num % i == 0]
    return sum(divisors) if divisors else 0