def all_left_right_truncatable_prime(nums):
    x = nums[35]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            left = int(s[i:])
            right = int(s[:len(s) - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = [n for n in range(2, x + 1) if '0' not in str(n) and is_truncatable(n)]
    return sorted(result, reverse=True)