def find_sum_of_multiples(n):
    """This function takes one argument, a positive integer, and returns the sum of
       the first 94 possitive multiples of the given integer."""
    if n <= 0:
        raise ValueError('Input number must be positive')
    result = 0
    for i in range(1, 95):
        result += i * n
    return result