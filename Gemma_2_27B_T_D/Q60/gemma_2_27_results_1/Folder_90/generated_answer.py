def all_left_right_truncatable_prime(nums):
    x = nums[466]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        s = str(n)
        while len(s) > 1:
            if not (is_prime(int(s)) and is_prime(int(s[:-1]))):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)], reverse=True)