def all_left_truncatable_prime(nums):
    x = nums[4]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        if '0' not in p_str:
            is_truncatable = True
            for i in range(1, len(p_str)):
                if int(p_str[i:]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(p)
    return sorted(truncatable_primes)