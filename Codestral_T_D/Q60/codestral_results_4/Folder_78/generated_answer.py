def all_left_right_truncatable_prime(nums):
    x = nums[23]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not (is_prime(int(str(n)[i:])) and is_prime(int(str(n)[:-i]))):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])