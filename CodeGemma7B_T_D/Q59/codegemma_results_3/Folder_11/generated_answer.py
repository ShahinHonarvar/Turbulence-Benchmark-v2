def all_left_truncatable_prime(args):
    """
  This function takes an argument which is a tuple of positive integers. Let x be the integer at index 86. The function should return the list of all left-truncatable prime numbers less than x. The return list should be sorted in ascending order. A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
  """
    x, = args

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    result.sort()
    return result