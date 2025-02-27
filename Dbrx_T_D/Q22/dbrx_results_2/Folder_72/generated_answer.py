def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError('Argument must be a positive integer')
    return sum(range(n, 88 * n, n))