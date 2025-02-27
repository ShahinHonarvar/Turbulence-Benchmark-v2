def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = nums[100]
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_left_truncatable(n) and is_right_truncatable(n)])