def all_left_truncatable_prime(nums):
    x = nums[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n == 0:
            return True
        if not is_prime(n):
            return False
        return is_left_truncatable_prime(int(str(n)[1:]))
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])