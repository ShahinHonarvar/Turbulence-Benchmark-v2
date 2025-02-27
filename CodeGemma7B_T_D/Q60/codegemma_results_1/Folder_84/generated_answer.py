def all_left_right_truncatable_prime(n):
    """
            Write a function called 'all_left_right_truncatable_prime' that takes one argument which is a tuple of positive integers.
            Let x be the integer at index 630. The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
            The return list should be sorted in descending order. If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
            A left-and-right-truncatable prime number is a prime number that contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n == 2 or n == 5:
            return True
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) % 2 == 0 or int(str_n[i:]) % 5 == 0:
                return False
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    result = []
    for i in range(n + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result