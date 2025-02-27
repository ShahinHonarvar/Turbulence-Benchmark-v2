def all_left_truncatable_prime(nums):
    x = nums[11]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 2, 2):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime_helper(num):
        if num == 0:
            return True
        if num % 10 == 0 or not is_prime(num):
            return False
        return left_truncatable_prime_helper(num // 10)
    return sorted([n for n in range(2, x) if is_prime(n) and left_truncatable_prime_helper(n)])