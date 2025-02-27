def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        right_truncatable = True
        n = p
        while n > 0:
            if n not in primes:
                right_truncatable = False
                break
            n //= 10
        if right_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)