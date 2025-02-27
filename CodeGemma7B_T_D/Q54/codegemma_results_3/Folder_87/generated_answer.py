def all_right_truncatable_prime(t):
    """
    Return sorted list of all right-truncatable prime numbers less than or equal to x.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    x = t[39]
    result = []
    for i in range(x - 1, 2, -1):
        if is_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)