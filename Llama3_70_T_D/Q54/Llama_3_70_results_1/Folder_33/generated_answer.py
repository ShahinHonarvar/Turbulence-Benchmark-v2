def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[:len(n) - i])):
                return False
        return True
    x = nums[945]
    return sorted([i for i in range(2, x) if is_right_truncatable(i) and is_prime(i)], reverse=True)