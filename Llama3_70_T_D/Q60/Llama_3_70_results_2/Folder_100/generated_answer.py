def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
            if not is_prime(int(n_str[:-i])):
                return False
        return True
    x = nums[26]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable(i)])