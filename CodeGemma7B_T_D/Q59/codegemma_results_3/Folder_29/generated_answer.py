def all_left_truncatable_prime(nums):
    """
          Given a tuple of positive integers, returns the list of left-truncatable
          prime numbers less than x.
          """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n % 10 == 0:
            return False
        for i in range(len(str(n)) - 1):
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    x = nums[55]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)