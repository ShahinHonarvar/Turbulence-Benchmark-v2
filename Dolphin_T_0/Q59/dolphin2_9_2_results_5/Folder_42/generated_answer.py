def all_left_truncatable_prime(t):
    x = t[64]
    primes = [2, 3, 5, 7]
    for p in primes:
        while p * p <= x:
            if x % p == 0:
                x //= p
            else:
                p += 2
    for num in range(max(primes), x - 1, -1):
        if all((num % p for p in primes)):
            trunc = num
            while trunc and all((trunc % p for p in primes)):
                trunc //= 10
            if trunc == 0:
                primes.append(num)
    return primes[::-1]