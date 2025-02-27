def all_left_right_truncatable_prime(numbers):
    """
    This function all_left_right_truncatable_prime returns the list of all left-and-right-truncatable prime numbers
    less than or equal to x.
    """

    def is_truncatable_prime(n):
        """
        This function is_truncatable_prime returns True if a number is a left-and-right-truncatable prime.
        """
        while n:
            if n % 10 in {0, 2, 4, 5, 6, 8}:
                return False
            if n != 3 and n % 3 in {0, 3, 4, 5, 7, 8, 9}:
                return False
            if n != 7 and n % 11 in {0, 4, 5, 6, 8, 9, 10}:
                return False
            n //= 10
            if n > 1 and n % 10 in {0, 1, 5, 6, 8, 9}:
                return False
        return True
    x = numbers[0]
    primes = []
    for possible_prime in range(x, 1, -1):
        if is_truncatable_prime(possible_prime):
            primes.append(possible_prime)
    return primes