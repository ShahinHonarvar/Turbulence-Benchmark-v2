def all_left_right_truncatable_prime(nums):
    x = nums[86]
    primes = [p for p in range(2, x + 1) if all((p % i for i in range(2, int(p ** 0.5) + 1)))]
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        if '0' not in p_str and all((int(p_str[i:]) in primes and int(p_str[:i + 1]) in primes for i in range(len(p_str) - 1))):
            truncatable_primes.append(p)
    return sorted(truncatable_primes)