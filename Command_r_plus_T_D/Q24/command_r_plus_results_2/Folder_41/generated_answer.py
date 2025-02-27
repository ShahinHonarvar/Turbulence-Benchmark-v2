def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer')
    divisors = [i for i in range(2, 5) if num % i == 0]
    return sum(divisors) if divisors else 0