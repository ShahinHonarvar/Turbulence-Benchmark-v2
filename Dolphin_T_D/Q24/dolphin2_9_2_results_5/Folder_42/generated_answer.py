def sum_of_divisors_in_range(n):
    assert n > 0, 'The input should be a positive integer'
    return sum((i for i in range(1, n + 1) if 14 <= i <= 93 and n % i == 0))