def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if '0' in str(n) or not is_prime(n):
                return False
            n //= 10
        return True
    x = nums[67]
    left_truncatable_primes = [n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n)]
    return left_truncatable_primes