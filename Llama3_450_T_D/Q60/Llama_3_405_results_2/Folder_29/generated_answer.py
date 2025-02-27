def all_left_right_truncatable_prime(nums):
    x = nums[55]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        digits = str(n)
        if '0' in digits:
            return False
        for i in range(len(digits)):
            left = int(digits[i:])
            right = int(digits[:-i or len(digits)])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)