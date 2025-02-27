def all_left_right_truncatable_prime(x):
    """
    This function takes a tuple of positive integers, and returns a list of all left-and-right-truncatable prime numbers that
    are less than or equal to the integer at index 3.
    """

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        while len(str(n)) > 2:
            if n % 10 == 0 or n // 10 % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n = (n // 10, n % 10)[::-1]
            n = int(''.join(map(str, n)))
        return is_prime(n)
    res = [i for i in range(1, x[3] + 1) if left_right_truncatable(i)]
    res.sort(reverse=True)
    return res