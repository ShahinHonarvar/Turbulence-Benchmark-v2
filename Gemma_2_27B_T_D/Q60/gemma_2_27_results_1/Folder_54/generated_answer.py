def all_left_right_truncatable_prime(nums):
    x = nums[88]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
            s = s[:-1]
        return is_prime(int(s))
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)