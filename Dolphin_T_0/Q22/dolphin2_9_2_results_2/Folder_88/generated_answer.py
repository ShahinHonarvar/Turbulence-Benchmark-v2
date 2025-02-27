def find_sum_of_multiples(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError('Input should be a positive integer')
    return sum((i for i in range(n, 24 * n + 1, n)))