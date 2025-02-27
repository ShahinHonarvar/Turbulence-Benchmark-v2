def all_right_truncatable_prime(nums):
    x = nums[37]
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
        p_str = str(p)
        is_right_truncatable = True
        for i in range(1, len(p_str)):
            if int(p_str[:-i]) not in primes:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes, reverse=True)