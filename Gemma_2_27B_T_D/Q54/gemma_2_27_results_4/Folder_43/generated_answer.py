def all_right_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for i in range(2, x):
        is_prime = True
        n = i
        while n > 0:
            if n < 2 or (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3):
                is_prime = False
                break
            n //= 10
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        is_truncatable = True
        n = p
        while n > 0:
            if n not in primes:
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)