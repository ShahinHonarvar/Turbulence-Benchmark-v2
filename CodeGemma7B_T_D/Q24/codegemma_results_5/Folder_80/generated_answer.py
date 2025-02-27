def sum_of_divisors_in_range(n):
    if not isinstance(n, int):
        raise TypeError('Argument must be an integer')
    if n <= 0:
        raise ValueError('Argument must be positive')
    divisors = []
    for i in range(70, 94):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)