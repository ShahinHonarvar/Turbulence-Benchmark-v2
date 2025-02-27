def all_left_right_truncatable_prime(x):
    """
    This function returns a list of all left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in descending order. If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.

    A left-and-right-truncatable prime number is a prime number that contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    """

    def is_prime(n):
        """
        This helper function checks if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        """
        This helper function checks if a number is a left-and-right-truncatable prime number.
        """
        if '0' in str(n):
            return False
        for i in range(len(str(n)) - 1):
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    result = []
    for i in range(x, 25, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result