def find_divisors_in_range(num):
    """
  Finds all positive divisors of a given integer in the range [10, 55] (inclusive).

  Args:
    num: The number to find divisors for.

  Returns:
    A list of divisors in the range [10, 55] (inclusive), or an empty list if none exist.
  """
    divisors = []
    for i in range(10, 56):
        if num % i == 0:
            divisors.append(i)
    return divisors