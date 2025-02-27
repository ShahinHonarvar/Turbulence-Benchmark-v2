def all_right_truncatable_prime(nums):
    x = nums[65]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    result = []
    for p in primes:
        truncatable = True
        n = str(p)
        while len(n) > 0:
            if int(n) not in primes:
                truncatable = False
                break
            n = n[:-1]
        if truncatable:
            result.append(p)
    return sorted(result, reverse=True)