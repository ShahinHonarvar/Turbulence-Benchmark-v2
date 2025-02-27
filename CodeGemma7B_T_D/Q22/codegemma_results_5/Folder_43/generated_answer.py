def find_sum_of_multiples(x):
    """
    Finds the sum of the first 74 positive multiples of a given integer.

    Args:
      x: A positive integer.

    Returns:
      The sum of the first 74 positive multiples of x.
    """
    sum = 0
    for i in range(1, 75):
        if i % x == 0:
            sum += i
    return sum