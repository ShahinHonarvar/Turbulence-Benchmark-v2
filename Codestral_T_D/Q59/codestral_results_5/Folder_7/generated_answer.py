def all_left_truncatable_prime(nums):
    x = nums[803]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    for n in range(2, x):
        if '0' not in str(n) and left_truncatable(n):
            primes.append(n)
    return sorted(primes)