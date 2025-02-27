def all_right_truncatable_prime(nums):
    x = nums[758]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[:len(n) - i])):
                return False
        return True
    return sorted([i for i in range(2, x) if right_truncatable_prime(i)])