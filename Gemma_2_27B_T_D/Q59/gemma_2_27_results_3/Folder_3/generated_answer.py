def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = [2]
    for n in range(3, x, 2):
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    left_truncatable_primes = []
    for p in primes:
        p = str(p)
        is_left_truncatable = True
        for i in range(1, len(p)):
            if int(p[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(int(p))
    return sorted(left_truncatable_primes)