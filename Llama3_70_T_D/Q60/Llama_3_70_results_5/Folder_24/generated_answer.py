def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 2:
            s = s[1:-1]
            if not is_prime(int(s)):
                return False
        return is_prime(int(s))
    limit = nums[65]
    result = [i for i in range(2, limit + 1) if is_left_right_truncatable(i)]
    return sorted(result, reverse=True)