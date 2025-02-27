def all_right_truncatable_prime(nums):
    x = nums[78]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for p in primes:
        right_truncatable = True
        p_str = str(p)
        for i in range(len(p_str) - 1, 0, -1):
            if int(p_str[:i]) not in primes:
                right_truncatable = False
                break
        if right_truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes, reverse=True)