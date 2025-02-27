def all_left_truncatable_prime(nums):
    x = nums[25]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        p_str = str(p)
        is_left_truncatable = True
        for i in range(1, len(p_str)):
            if int(p_str[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes