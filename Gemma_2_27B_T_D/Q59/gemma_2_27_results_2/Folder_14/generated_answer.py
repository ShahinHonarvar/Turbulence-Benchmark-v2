def all_left_truncatable_prime(nums):
    x = nums[78]
    isPrime = [True] * x
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, x, i):
                isPrime[j] = False
    primes = [i for i, p in enumerate(isPrime) if p]
    left_truncatable_primes = []
    for prime in primes:
        if prime < x:
            prime_str = str(prime)
            is_truncatable = True
            for i in range(1, len(prime_str)):
                if not isPrime[int(prime_str[i:])]:
                    is_truncatable = False
                    break
            if is_truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)