def find_sum_of_multiples(n):
    """Returns the sum of the first 100 positive multiples of a given integer."""
    return sum((n * i for i in range(1, 101)))