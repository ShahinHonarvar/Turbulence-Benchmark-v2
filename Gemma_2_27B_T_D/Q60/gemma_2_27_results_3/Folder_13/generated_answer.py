def all_left_right_truncatable_prime(nums):
    x = nums[784]

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
        while n > 9:
            n = str(n)
            if not is_prime(int(n)) or not is_prime(int(n[1:])):
                return False
            n = int(n[1:-1])
        return is_prime(n)
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)])