def all_left_truncatable_prime(x):
    """
    This function takes an argument which is a tuple of positive integers.
    Let x be the integer at index 29.
    The function should return the list of all left-truncatable prime numbers less than x.
    The return list should be sorted in ascending order.
    """

    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    result = []
    for i in range(2, x):
        if not (is_prime(i) and '0' not in str(i)):
            continue
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            result.append(i)
    result.sort()
    return result