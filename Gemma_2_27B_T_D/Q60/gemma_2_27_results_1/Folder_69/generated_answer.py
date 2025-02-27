def all_left_right_truncatable_prime(nums):
    x = nums[760]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1, 2):
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
        is_truncatable = True
        while len(p_str) > 1:
            p_str = p_str[1:]
            if int(p_str) not in primes:
                is_truncatable = False
                break
        p_str = str(p)
        while len(p_str) > 1:
            p_str = p_str[:-1]
            if int(p_str) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)