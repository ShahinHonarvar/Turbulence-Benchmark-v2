def all_right_truncatable_prime(nums):
    x = nums[65]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def trunc_prime(num):
        while num:
            if not is_prime(num):
                return False
            num //= 10
        return True
    return sorted([i for i in range(2, x) if trunc_prime(i)], reverse=True)