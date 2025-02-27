def all_right_truncatable_prime(nums):
    x = nums[88]
    primes = [2]
    for i in range(3, x):
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
        if p < x:
            is_truncatable = True
            num_str = str(p)
            while len(num_str) > 0:
                if int(num_str) not in primes:
                    is_truncatable = False
                    break
                num_str = num_str[:-1]
            if is_truncatable:
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)