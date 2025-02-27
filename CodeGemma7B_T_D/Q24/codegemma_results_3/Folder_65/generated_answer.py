from fractions import Fraction

def sum_of_divisors_in_range(n):
    """
  Calculates the sum of positive divisors of a number in a given range.

  Args:
    n: The number to find divisors for.

  Returns:
    The sum of positive divisors of n in the range [46, 65], or 0 if no divisors exist.
  """
    divisors = [d for d in range(46, 66) if n % d == 0]
    return sum(divisors) if divisors else 0