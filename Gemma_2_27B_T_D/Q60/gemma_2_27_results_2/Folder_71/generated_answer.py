def all_left_right_truncatable_prime(nums):
    x = nums[22]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i) and '0' not in str(i)])[::-1]