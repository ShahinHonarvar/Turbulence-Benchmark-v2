def all_right_truncatable_prime(x):
    """
    Write a function called 'all_right_truncatable_prime' that takes an argument which is a tuple of positive integers.
    Let x be the integer at index 46. The function should return the sorted list of all right-truncatable prime numbers less than x.
    The returned list should be sorted in descending order. If there is no such right-truncatable prime number, the function should return an empty list.
    A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    """
    Imports = 'import math'

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def is_right_truncatable_prime(x):
        if not is_prime(x):
            return False
        while x > 0:
            x //= 10
            if x > 1 and (not is_prime(x)):
                return False
        return True
    res = []
    for num in x:
        if is_right_truncatable_prime(num):
            res.append(num)
    return sorted(res, reverse=True)