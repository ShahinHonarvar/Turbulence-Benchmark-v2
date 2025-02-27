def all_left_truncatable_prime(nums):
    x = nums[992]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        is_truncatable = True
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if int(prime_str[i:]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)