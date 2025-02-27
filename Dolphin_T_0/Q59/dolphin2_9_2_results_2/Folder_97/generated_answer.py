def all_left_truncatable_prime(nums):
    x = nums[645]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return False
        return True

    def is_truncatable_prime(n):
        if not set(str(n)).issubset('123456789'):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(x) if is_truncatable_prime(n)])