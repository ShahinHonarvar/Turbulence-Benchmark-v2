def all_left_truncatable_prime(nums):
    x = nums[81]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)