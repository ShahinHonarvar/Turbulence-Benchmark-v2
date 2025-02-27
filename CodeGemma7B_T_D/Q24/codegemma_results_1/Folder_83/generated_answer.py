def sum_of_divisors_in_range(n):
    """Calculates the sum of divisors in a given range.

    Args:
      n: A positive integer.

    Returns:
      The sum of positive divisors of n in the range [5, 7], or 0 if no such divisors exist.
    """
    sum_divisors = 0
    for i in range(5, 8):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors