def all_left_truncatable_prime(nums):
    x = nums[94]
    primes = [2, 3, 5, 7]
    for i in range(2, int(x ** 0.5) + 1):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        is_left_truncatable = True
        s = str(p)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable and p < x:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)