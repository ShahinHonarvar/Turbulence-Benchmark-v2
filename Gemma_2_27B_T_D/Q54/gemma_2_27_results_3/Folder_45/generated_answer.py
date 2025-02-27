def all_right_truncatable_prime(nums):
    x = nums[61]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        n = i
        is_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)