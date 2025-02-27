def find_divisors_in_range(n):
    """
  This function finds all positive divisors of the given integer n that are
  between 11 and 56 (inclusive). It returns a list of these divisors, or an
  empty list if no such divisors exist.
  """
    divisors = []
    for i in range(11, 57):
        if n % i == 0:
            divisors.append(i)
    return divisors