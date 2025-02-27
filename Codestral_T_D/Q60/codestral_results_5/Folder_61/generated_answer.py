def all_left_right_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        while n:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)], reverse=True)