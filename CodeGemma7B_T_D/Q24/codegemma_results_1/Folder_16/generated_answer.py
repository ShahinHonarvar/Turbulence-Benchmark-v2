def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input must be positive.')
    if not isinstance(n, int):
        raise TypeError('Input must be an integer.')
    if not 228 <= n <= 846:
        raise ValueError('Input must be between 228 and 846, inclusive.')
    divisors = []
    for i in range(228, 847):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)