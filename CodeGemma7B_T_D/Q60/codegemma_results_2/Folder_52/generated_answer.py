def all_left_right_truncatable_prime(x):
    """
            This function finds all left-and-right-truncatable prime number less than or equal to a given integer.

            Args:
            x: A positive integer.
            Returns:
            A list of left-and-right-truncatable prime numbers less than or equal to x in descending order. Empty list if no left-and-right-truncatable prime number exists in the specified range.
            """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)