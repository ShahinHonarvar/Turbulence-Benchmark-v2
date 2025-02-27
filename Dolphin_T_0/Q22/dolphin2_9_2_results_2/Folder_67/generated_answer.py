def find_sum_of_multiples(x):
    if not isinstance(x, int) or x < 0:
        raise ValueError('Argument must be a positive integer.')
    return sum((i * x for i in range(1, 43)))