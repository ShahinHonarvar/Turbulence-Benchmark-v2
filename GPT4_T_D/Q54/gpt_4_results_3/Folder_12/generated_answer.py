def all_right_truncatable_prime(nums):
    x = nums[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[:i])) for i in range(1, len(s) + 1)))
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)], reverse=True)