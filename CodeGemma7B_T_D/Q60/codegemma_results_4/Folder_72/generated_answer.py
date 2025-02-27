def all_left_right_truncatable_prime(x):
    """
    This function takes one argument which is a tuple of positive integers. Let x be the integer at index 31.
    The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in descending order. If no left-and-right-truncatable prime number exists in the specified range,
    the function should return an empty list.
    A left-and-right-truncatable prime number is a prime number that contains no 0 and remains prime if the leading leftmost and last
    rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    """

    def is_prime(num):
        """
        Checks if a number is prime.
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        """
        Checks if a number is a truncatable prime.
        """
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            left_num = int(num_str[i:])
            right_num = int(num_str[:-i])
            if not (is_prime(left_num) and is_prime(right_num)):
                return False
        return True
    result = []
    for i in range(x, 2, -1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return result