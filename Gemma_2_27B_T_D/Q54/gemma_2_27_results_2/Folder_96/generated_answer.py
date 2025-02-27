def all_right_truncatable_prime(nums):
    x = nums[29]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        truncatable = True
        n = str(num)
        while len(n) > 0:
            if not is_prime(int(n)):
                truncatable = False
                break
            n = n[:-1]
        if truncatable:
            primes.append(num)
    return sorted(primes)