import math

def all_right_truncatable_prime(n):
    """
    A function that returns the sorted list of all right-truncatable prime numbers less than x.

    The function takes an argument which is a tuple of positive integers. Let x be the integer at index 22.

    The function returns an empty list if there is no such right-truncatable prime number.

    A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.

    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    ans = []
    for i in range(1, n[22]):
        if right_truncatable_prime(i):
            ans.append(i)
    return sorted(ans, reverse=True)