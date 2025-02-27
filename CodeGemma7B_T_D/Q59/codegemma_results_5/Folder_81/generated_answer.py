def all_left_truncatable_prime(num):
    """
            A function that takes an argument which is a tuple of positive integers. Let x be the integer at index 98. The function should return the list of all left-truncatable prime numbers less than x. The return list should be sorted in ascending order. A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
            """
    maximum = num[98]

    def is_prime(n):
        if n == 1:
            return False
        for a in range(2, int(n ** 0.5) + 1):
            if n % a == 0:
                return False
        return True

    def left_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    result = []
    for n in range(2, maximum):
        if is_prime(n) and left_truncatable(n):
            result.append(n)
    result.sort()
    return result