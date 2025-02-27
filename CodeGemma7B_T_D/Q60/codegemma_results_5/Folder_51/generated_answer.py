def all_left_right_truncatable_prime(n):
    """
    Return a list of all left-and-right-truncatable prime numbers less than or equal to x
    """

    def is_prime(n):
        """
        Return True if n is a prime number, otherwise False
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        """
        Return True if n is a left-and-right-truncatable prime number, otherwise False
        """
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])):
                return False
            if not is_prime(int(str(n)[-i:])):
                return False
        return True
    list_prime = []
    for i in range(2, n + 1):
        if is_truncatable_prime(i):
            list_prime.append(i)
    return sorted(list_prime)