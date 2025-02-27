def all_right_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = []
    for prime in primes:
        is_right_truncatable = True
        prime_str = str(prime)
        while len(prime_str) > 1:
            prime_str = prime_str[:-1]
            if not int(prime_str) in primes:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            result.append(prime)
    return sorted(result)