def all_left_truncatable_prime(nums):
    x = nums[7]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return is_prime(int(n))
    for i in range(2, x):
        if is_left_truncatable(i):
            primes.append(i)
    return sorted(primes)