def all_right_truncatable_prime(x):
    """
    Write a function called 'all_right_truncatable_prime' that takes an argument which is a tuple of positive integers.
    Let x be the integer at index 36. The function should return the sorted list of all right-truncatable prime numbers less than x.
    The returned list should be sorted in descending order.
    If there is no such right-truncatable prime number, the function should return an empty list.
    A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    limit = x - 1
    truncatable_primes = []
    for n in range(2, limit + 1):
        if is_prime(n) and right_truncatable(n):
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes