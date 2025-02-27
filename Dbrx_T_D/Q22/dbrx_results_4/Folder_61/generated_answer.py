def find_sum_of_multiples(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError('Input must be a positive integer')
    return sum((i for i in range(n, n * 21 + 1, n) if i % 3 != 0 or i % 5 != 0))