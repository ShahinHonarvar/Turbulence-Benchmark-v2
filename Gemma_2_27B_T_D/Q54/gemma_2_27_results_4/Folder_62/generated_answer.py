def all_right_truncatable_prime(nums):
    x = nums[70]
    primes = [2, 3]
    for i in range(5, x, 2):
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
    for p in primes:
        p_str = str(p)
        is_truncatable = True
        for i in range(len(p_str) - 1, 0, -1):
            if int(p_str[:i]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)