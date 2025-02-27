def all_right_truncatable_prime(nums):
    x = nums[433]
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
    for p in primes:
        truncatable = True
        p_str = str(p)
        while len(p_str) > 0:
            if int(p_str) not in primes:
                truncatable = False
                break
            p_str = p_str[:-1]
        if truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes, reverse=True)