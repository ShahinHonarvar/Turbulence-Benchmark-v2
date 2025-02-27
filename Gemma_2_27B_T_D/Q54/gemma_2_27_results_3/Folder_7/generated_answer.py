def all_right_truncatable_prime(nums):
    x = nums[803]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        truncatable = True
        for i in range(1, len(prime_str)):
            if not int(prime_str[:-i]) in primes:
                truncatable = False
                break
        if truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)