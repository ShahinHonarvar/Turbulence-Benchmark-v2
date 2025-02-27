def all_left_right_truncatable_prime(nums):
    x = nums[64]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            if not is_prime(int(n_str)) or '0' in n_str:
                return False
            n_str = n_str[1:-1]
        return True
    return sorted([num for num in range(x, 1, -1) if is_truncatable_prime(num)], reverse=True)