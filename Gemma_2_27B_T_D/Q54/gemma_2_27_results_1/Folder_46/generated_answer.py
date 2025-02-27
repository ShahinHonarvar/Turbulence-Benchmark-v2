def all_right_truncatable_prime(nums):
    x = nums[33]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        is_truncatable = True
        temp = prime
        while temp > 0:
            if temp not in primes:
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)