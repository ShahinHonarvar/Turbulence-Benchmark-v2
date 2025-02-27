def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:len(s) - i])):
                return False
        return True
    limit = nums[98]
    return sorted([i for i in range(2, limit) if is_right_truncatable(i)])