def find_sum_of_multiples(x):
    """Return the sum of the first 366 multiples of x"""
    return sum(range(x, x + 367 * x, x))