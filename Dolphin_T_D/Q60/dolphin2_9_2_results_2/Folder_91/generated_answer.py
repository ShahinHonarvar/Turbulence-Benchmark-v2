def all_left_right_truncatable_prime(x):
    """
    Return a list of all left-and-right-truncatable prime numbers less than or equal to x.
    The list is sorted in descending order.
    """

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def istruncatable(n, i=0):
        if len(str(n)) == 1 or i > len(str(n)) - 2:
            return True
        if n // 10 ** i % 10 == 0 or n % 10 ** (len(str(n)) - i - 1) % 10 == 0:
            return False
        return istruncatable(n // 10, i + 1) and istruncatable(n % 10 ** len(str(n)) - i, i)
    result = [n for n in range(x + 1) if isprime(n) and istruncatable(n)]
    return sorted(result, reverse=True)