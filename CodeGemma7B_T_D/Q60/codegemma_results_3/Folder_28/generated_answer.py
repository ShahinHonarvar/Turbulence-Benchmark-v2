def all_left_right_truncatable_prime(n):
    """
            Returns a sorted list of all left-and-right-truncatable prime numbers less than or equal to n.
            """

    def is_prime(n):
        """
                Checks if n is a prime number.
                """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        """
                Checks if n is a truncatable prime number.
                """
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    result = []
    for i in range(3, n + 1, 2):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return result