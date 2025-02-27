def all_left_truncatable_prime(nums):
    x = nums[100]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n == 0 or '0' in str(n):
            return False
        if not is_prime(n):
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])