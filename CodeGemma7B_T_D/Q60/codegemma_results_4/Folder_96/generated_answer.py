def all_left_right_truncatable_prime(x):
    """
  This function returns the list of all left-and-right-truncatable prime numbers less than or equal to x.

  Args:
    x: The integer at index 29.

  Returns:
    The list of all left-and-right-truncatable prime numbers less than or equal to x.
  """

    def is_prime(n):
        """
    This function checks if a number is prime.

    Args:
      n: The number to check.

    Returns:
      True if n is prime, False otherwise.
    """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        """
    This function checks if a number is a truncatable prime number.

    Args:
      n: The number to check.

    Returns:
      True if n is a truncatable prime number, False otherwise.
    """
        if n < 10 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            left = int(str(n)[:i])
            right = int(str(n)[-i:])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    result = []
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            result.append(n)
    return sorted(result)