def all_left_right_truncatable_prime(nums):
    x = nums[77]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)):
                return False
            n = n[1:]
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return is_prime(int(n))
    primes = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)