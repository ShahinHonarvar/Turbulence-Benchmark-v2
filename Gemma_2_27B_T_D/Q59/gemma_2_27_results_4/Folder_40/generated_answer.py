def all_left_truncatable_prime(nums):
    x = nums[10]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)