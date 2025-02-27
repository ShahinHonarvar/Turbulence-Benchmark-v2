def all_right_truncatable_prime(numbers):
    """
    This function takes a tuple of positive integers as input, and returns a sorted list of
    all right-truncatable prime numbers less than the integer at index 70 of the input tuple.
    If no such right-truncatable prime number exists, an empty list is returned.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[70]
    return sorted([n for n in range(1, x) if is_right_truncatable_prime(n)])