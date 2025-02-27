def all_right_truncatable_prime(nums):
    x = nums[11]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x):
        n = i
        right_truncatable = True
        while n > 0:
            if not is_prime(n):
                right_truncatable = False
                break
            n //= 10
        if right_truncatable:
            primes.append(i)
    return sorted(primes)