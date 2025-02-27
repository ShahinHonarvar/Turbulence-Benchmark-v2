def all_left_truncatable_prime(nums):
    x = nums[945]
    primes = [2]
    for i in range(3, x, 2):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        str_p = str(p)
        is_truncatable = True
        for i in range(1, len(str_p)):
            if int(str_p[i:]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)