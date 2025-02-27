def all_left_truncatable_prime(t):
    x = t[126]
    primes = [2]
    left_truncatable_primes = []
    for i in range(3, x):
        if all((i % p > 0 for p in primes)):
            primes.append(i)
            num = i
            while num > 0:
                num = num // 10
                if num > 0 and num not in primes:
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)