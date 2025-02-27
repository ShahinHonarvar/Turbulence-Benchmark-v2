def all_left_right_truncatable_prime(nums):
    x = nums[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return n // 10 > 0 and n % 10 > 0 and is_prime(n // 10) and is_prime(n % 10)
    return [num for num in range(2, x + 1) if is_truncatable(num)]