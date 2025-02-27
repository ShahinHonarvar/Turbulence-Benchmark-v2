def find_sum_of_multiples(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Input argument must be a positive integer.')
    return sum((i * n for i in range(1, 189)))