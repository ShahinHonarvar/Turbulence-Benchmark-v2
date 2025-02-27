def all_left_right_truncatable_prime(x):
    """
    A function that takes one argument which is a tuple of positive integers.
    Let x be the integer at index 3. The function should return the list of all
    left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in descending order. 
    If no left-and-right-truncatable prime number exists in the specified range,
    the function should return an empty list.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        for i in range(len(str(n)) - 1, 0, -1):
            if int(str(n)[i]) == 0 or not is_prime(int(str(n)[1:i + 1])) or (not is_prime(int(str(n)[i:]))):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True)