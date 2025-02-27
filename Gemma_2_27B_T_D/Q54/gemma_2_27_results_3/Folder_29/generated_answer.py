def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(2, x):
        if all((num != 0 and i % num for num in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        truncatable = True
        p_str = str(p)
        while len(p_str) > 0:
            if int(p_str) not in primes:
                truncatable = False
                break
            p_str = p_str[:-1]
        if truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)